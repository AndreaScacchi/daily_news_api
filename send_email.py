import smtplib, ssl
import config

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    
    username = config.username
    app_password = config.email_password
    
    receiver = config.username
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, app_password)
        server.sendmail(username, receiver, message)