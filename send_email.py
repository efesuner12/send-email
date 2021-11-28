import smtplib, ssl

FROM_EMAIL_ADDRESS = "####@gmail.com"
FROM_EMAIL_PASSWORD = "####"
port = 587
smtp_server = "smtp.gmail.com"
message = "hi!"

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(FROM_EMAIL_ADDRESS, FROM_EMAIL_PASSWORD)
    server.sendmail(FROM_EMAIL_ADDRESS, FROM_EMAIL_ADDRESS, message)
    
