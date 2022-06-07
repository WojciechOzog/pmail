#!/usr/bin/python3.8

import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# configure
sender = 'test@test.pl'
subject = 'testowy'
recipient = 'wojt.ozog@gmail.com'
server = '10.10.10.25'
message = 'no i juz'


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
