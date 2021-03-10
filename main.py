import sba
import mailsender


if __name__ == '__main__':
    sba = sba.Sba("solarwinds orion username", "password")
    sba.login()
    alarms = sba.get_progress_data()

    # Alarm üreten lokasyonlar
    location = "Lokasyon \t İnterface \t  receive \t transmit \t \n"

    if len(alarms) > 0:
        for loc in alarms:
            location = location + loc + "\n"

        mailsender.send_mail(location)

    sba.close()