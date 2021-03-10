
from smtplib import SMTP
from email.mime.text import MIMEText


def send_mail(self, message):
    #  İçerik
    subject = "SBA Botu Alarm"
    content = message

    #  Account
    from_ = "gönderen eposta"
    to_ = "alıcı eposta"
    passwd = "gönderen eposta pass"

    # Mail gönder
    mail = MIMEText(content, "utf-8")
    mail["From"] = from_
    mail["To"] = to_
    mail["Subject"] = subject
    mail = mail.as_string()
    smtp = SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login(from_, passwd)
    smtp.sendmail(from_, to_, mail)





