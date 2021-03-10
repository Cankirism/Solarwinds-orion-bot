from selenium import webdriver
import time


class Sba:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()

    def login(self):
        # username input
        self.browser.get("solarwinds orion url")
        self.browser.find_element_by_id(
            "ctl00_BodyContent_Username").send_keys(self.username)

        # password input
        self.browser.find_element_by_xpath(
            "//*[@id='ctl00_BodyContent_Password']").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element_by_xpath(
            "//*[@id='ctl00_BodyContent_LoginButton']").click()

        time.sleep(1)

    def get_progress_data(self):
        """
        Sayfa yüklendiğinde progressbar değerleri
        çekilirken bekleme yapmak gerekiyor
        AKsi halde 'No such element' hatası alınabilir.
        """
        time.sleep(10)

        # node bilgisi(lokasyon)
        node = self.browser.find_elements_by_xpath(
            "//*[@id='Resource6645_ctl00_ctl01_Wrapper_resContent']/table/tbody/tr/td[2]/a")

        # interface bilgisi
        interface = self.browser.find_elements_by_xpath(
            "//*[@id='Resource6645_ctl00_ctl01_Wrapper_resContent']/table/tbody/tr/td[4]/a")

        # receive
        receive = self.browser.find_elements_by_xpath(
            "//*[@id='Resource6645_ctl00_ctl01_Wrapper_resContent']/table/tbody/tr/td[5]/a[2]")

        # transmit
        transmit = self.browser.find_elements_by_xpath(
            "//*[@id='Resource6645_ctl00_ctl01_Wrapper_resContent']/table/tbody/tr/td[6]/a[2]")

        bandwidth_critical_locations = []

        for i in range(len(node)):
            received_transmitted_info = self.received_trasmitted_calculator(receive[i].text, transmit[i].text)
            if (received_transmitted_info["received"] >= 80 or received_transmitted_info["transmitted"] >= 80):
                bandwidth_critical_locations.append(
                    f"{node[i].text} \t {interface[i].text} \t {receive[i].text} \t {transmit[i].text}")

        return bandwidth_critical_locations

    def progress_text_splitter(self, text):
        # yüzdeli verilerden yüzde kısmı atlıyor
        splitted = str(text).split(" ")
        return splitted[0]

    def received_trasmitted_calculator(self, received, transmitted):
        # transmit ve received verileri dict yapısında return ediliyor
        received = self.progress_text_splitter(received)
        transmitted = self.progress_text_splitter(transmitted)
        return {"received": int(received), "transmitted": int(transmitted)}

    def close(self):
        self.browser.quit()   # Driver sonlandır
