from dotenv import load_dotenv
from email.message import EmailMessage
import os
import ssl
import smtplib
import sys


if len(sys.argv) != 3:
    print("Error: missing arg")
    sys.exit(1)

id = sys.argv[1]
body_content = sys.argv[2]


load_dotenv()
email_sender = os.environ["EMAIL_SENDER"]
email_password = os.environ["EMAIL_PASSWORD"]
email_reciever = 'asarda@mailinator.com'

subject = "Sent from github actions"
body = f"Id:{id}:::{body_content}"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())

print("Email sent")