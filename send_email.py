from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv
load_dotenv()

import os

def send_email(email, height,average_height,count):
    from_email= os.environ.get('ACCOUNT_EMAIL')
    from_password=os.environ.get('ACCOUNT_PASSWORD')
    to_email=email

    subject="Height data"
    message="Hey there, your height is <strong>%s</strong>cm.The average height of our user base is <strong>%s</strong>cm from a total of <strong>%s</strong> users." %(height, average_height, count)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)

