#!/usr/bin/python
# by lunaferie
# v1.1

import smtplib

# CONFIGURE:

fromaddr = 'user@yourdomain.com'
toaddr = 'user2@example.com'
subject = 'your msg subject'

text = 'This is a txt msg from Shire'

server = 'localhost'


#############################################

def pmail(fromaddr, toaddr, subject, text, server):
    msg = "\r\n".join([
        "From: %s" % fromaddr,
	"To: %s" % toaddr,
	"Subject: %s" % subject,
	"", 
	"%s" % text
	])

    try:
	s = smtplib.SMTP(server)
	s.sendmail(fromaddr, toaddr, msg)
	s.quit()
	print "INFO: message was sent"

    except smtplib.SMTPException:
	print "ERROR: unable to sent email"

pmail(fromaddr, toaddr, subject, text, server)
