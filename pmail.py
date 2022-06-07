#!/usr/bin/python3.8

import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# configure
sender = 'me@me.com'
subject = 'I want You'
recipient = 'you@you.com'
server = '127.0.0.1'
message = 'now'


def send_mail(sender, subject, recipient, server, message):
    msg = MIMEMultipart()
    msg.attach(MIMEText(message, "plain", "utf-8"))
    msg['from'] = ('wozog@test.pl')
    msg['subject'] = '{}'.format(subject)
    msg['to'] = '{}'.format(recipient)
    msg['Content-Type'] = 'text/plain; charset="utf-8"'
    try:
        s = smtplib.SMTP('{}'.format(server))
        s.ehlo()
        s.sendmail(sender, recipient, msg.as_string())
        s.quit()
        print ('INFO: mail was sent')
    except Exception as err:
        print ('ERROR {0}'.format(err))
        sys.exit(1)

send_mail(sender, subject, recipient, server, message)
