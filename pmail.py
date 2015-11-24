#!/usr/bin/python
# by lunaferie
# v2.2

import getopt
import sys
import smtplib
import email
from email.MIMEText import MIMEText

#### configure pmail:

# disable/enable debug level (0=OFF, 1=ON)
debug_level = 1


##### default message CONFIG:

subject = 'python test using pmail'
text = 'This is a txt msg from Shire'
server = 'localhost'

##### command lines arguments:

fromaddr = ''
toaddr = ''
at = []
auth = []

try:
    shortargs = "f:r:s:t:a:l:p:"
    longargs = ['server=', 'help']
    options, args = getopt.gnu_getopt(sys.argv[1:], shortargs, longargs)
except getopt.GetoptError as err:
    print str(err)
    print 'use --help'
    sys.exit(2)

for chose, value in options:
    if chose == '-f':
	fromaddr = value
    if chose == '-r':
	toaddr = value
    if chose == '-s':
	subject = value
    if chose == '-t':
	text = value
    if chose == '-a':
	file_path = value
	at.append(1)
    if chose == '-l':
	login = value
	auth.append(1)
    if chose == '-p':
	password = value
	auth.append(1)
    if chose == '--server':
	server = value
	print value
    if chose == '--help':
	print "pmail is an SMTP client"
	print '-f \t\t from address (REQUIRED)'
    	print '-r \t\t reciepent (REQUIRED)'
    	print '-s \t\t subject use "" (other than the default)'
    	print '-t \t\t text messages use "" (other than the default)'
    	print '-a \t\t add attachment filename (if required)'
    	print '-l \t\t login (if required)'
    	print '-p \t\t password (if required)'
    	print '--server	 change server (default: localhost)'
	sys.exit(0)

if not fromaddr or not toaddr:
   print "use -f \t\t - define your sender addres"
   print "use -r \t\t - define recipient"
   print "or \t\t --help"
   sys.exit(1)


#############################################

if len(at) > 0:
    f = file(file_path, 'rb')
    attachment = MIMEText(f.read())
    attachment.add_header('Content-Disposition', 'attachment', file_path=file_path)   
    f.close()
else:
    attachment = ''

msg = "\r\n".join([
#    "%s" % attachment,
    "From: %s" % fromaddr,
    "To: %s" % toaddr,
    "Subject: %s" % subject,
    "%s" % attachment,
    "", 
    "%s" % text
    ])

try:
    s = smtplib.SMTP(server)
    if debug_level == 1:
        s.set_debuglevel(True)
    else:
	pass
    if len(auth) > 0:
        s.login(login, password)
    else:
	pass
    s.ehlo()
    s.sendmail(fromaddr, toaddr, msg)
    s.quit()
    print "INFO: message was sent"

except Exception as err:
    print "ERROR %s" % str(err)
