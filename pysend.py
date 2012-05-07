###############################
# file pysend.py              #
# author Nanak Tattyrek       #
# version 0.1                 #
###############################

###############################################################
# This program lets you send any amount of emails             #
# to an address of your choice.                               #
#                                                             #
# THIS PROGRAM IS INTENDED TO BE A PRANKING TOOL              #
#                                                             #
# DO NOT USE THIS PROGRAM TO SEND SPAM MAILS                  #
#                                                             #
# I AM NOT RESPONSIBLE FOR ANY DAMAGE MADE WITH THIS TOOL     #
# (INLUDING BLOCKED GMAIL ACCOUNTS)                           #
#                                                             #
# Have fun ;)                                                 #
###############################################################

import smtplib
import datetime
import getpass


gmail_user = input('Gmail Username: ')
gmail_pwd = getpass.getpass()
to = input('Who do you want to prank? ')
subject = input('Enter subject: ')
text = input('Enter text: ')

count = int(input("How many mails do you want to send? "))

print("Sending {0} emails from {1}@gmail.com to {2}".format(count, gmail_user, to))

date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )

msg = "From: {0}@gmail.com\nTo: {1}\nSubject: {2}\nDate: {3}\n\n{4}".format( gmail_user, to, subject, date, text )

i = 0
while i < count:
	
	mailServer = smtplib.SMTP("smtp.gmail.com", 587)
	mailServer.ehlo()
	mailServer.starttls()
	mailServer.ehlo()
	mailServer.login(gmail_user, gmail_pwd)
	mailServer.sendmail(gmail_user, to, msg)
	mailServer.close()
	
	i+=1
