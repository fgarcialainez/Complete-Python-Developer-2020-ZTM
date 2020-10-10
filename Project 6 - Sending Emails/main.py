"""
This module implements the email sender exercise of the Section 17 of the course.
"""

import smtplib

from pathlib import Path
from string import Template
from email.message import EmailMessage


def send_email():
    # Create the email message
    email = EmailMessage()
    email['from'] = 'Felix Garcia Lainez'
    email['to'] = '<to email address>'
    email['subject'] = 'You won 1,000,000 dollars!'

    # Load the attachment html file and replace
    # the placerholder by the destinatary name
    html = Template(Path('index.html').read_text())
    email.set_content(html.substitute({'name': 'Alice'}), 'html')

    # Send the email via Gmail
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('<your email address>', '<your password>')
        smtp.send_message(email)

        print('Email sent!')


# Entry point of the script
if __name__ == '__main__':
    # Call the send email function
    send_email()
