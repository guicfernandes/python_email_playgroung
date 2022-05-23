import smtplib
import getpass
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
smtp_server = 'smtp.gmail.com'
port = 587
sender = 'guicfdev@gmail.com'
# guidev123@
pass_sender = getpass.getpass(prompt='Password: ', stream=None)
email = EmailMessage()
email['from'] = 'Guilherme Fernandes'
email['to'] = 'guilhermecfsp@gmail.com'
email['subject'] = 'You won 1,000,000 dollars'

# email.set_content('I am a Python Master!')
email.set_content(
    html.substitute(name='Tintin'),
    'html'
)

with smtplib.SMTP(host=smtp_server, port=port) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender, pass_sender)
    smtp.send_message(email)
    print('all good boss!')
