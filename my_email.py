# Project: Email Sender using SMTP
import smtplib
import ssl
from email.message import EmailMessage

SENDER = "souvikdan925@gmail.com"
PASSWORD = "gkrs eyvu pkzl rcde" #  enter your own App Password (Not Gmail Password)
RECEIVER = "souvikdan910@gmail.com"

msg = EmailMessage()
msg["From"] = SENDER
msg["To"] = RECEIVER
msg["Subject"] = "Automated Email from Python"
msg.set_content("Hello, I am Souvik. This email was sent using Python script by souvik.")

context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER, PASSWORD)
        server.send_message(msg)
    print("Email Sent Successfully!")

except Exception as e:
    print("Error:", e)