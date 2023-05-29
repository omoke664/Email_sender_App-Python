import smtplib
import ssl
from email.message import EmailMessage
from app2 import password

email_sender = 'senderemail@gmail.com'
email_password = password

email_receiver = 'receivermail@gmail.com'

subject = "Email subject goes here..."
body = """
The body of the email goes here...
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)
