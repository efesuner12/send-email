import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

fromaddr = "###@gmail.com"
password = "###"

def send():
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['Subject'] = "trial"
    body = "hello"
    msg.attach(MIMEText(body, 'plain'))

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, password)
    text = msg.as_string()

    s.sendmail(fromaddr, fromaddr, text)
    s.quit()


if __name__ == "__main__":
    send()
