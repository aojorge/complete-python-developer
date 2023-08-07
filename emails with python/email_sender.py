import smtplib
import ssl
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('./index.html').read_text())
email_sender = 'cangabr@gmail.com'
email_password = 'eqchracucakxmyje'
email_receiver = 'cangabr@hotmail.com'

subject = 'Isso é um email de teste em Python'
body = """
Estamos testando o envio de emails com Python.
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(html.substitute({'name':'Anderson'}), 'html')

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    print('Email enviado!')
