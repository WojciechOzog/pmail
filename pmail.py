#!/usr/bin/python
# v1.0

import smtplib

# CONFIGURE:

fromaddr = 'test@ayum.eu'
toaddr = 'wojt.ozog@gmail.com'
subject = 'test msg'

text = 'This is a txt mesg from shire'

server = 'localhost'


#############################################

def sendmail(fromaddr, toaddr, subject, text, server):
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

sendmail(fromaddr, toaddr, subject, text, server)
