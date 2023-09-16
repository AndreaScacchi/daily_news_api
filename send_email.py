import smtplib, ssl
import config

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    
    username = "andreascacchi10@gmail.com"
    email_password = config.email_password
    
    receiver = "andreascacchi10@gmail.com"
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, email_password)
        server.sendmail(username, receiver, message)