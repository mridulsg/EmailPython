import smtplib
'''
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 '''
from email import *
fromadr = input("Enter Source Address")
toadr= input("Enter destination Address")
 
message = MIMEMultipart()
 
message['From'] = fromadr
message['To'] = toadr
message['Subject'] = "Test python email with attachment"
 
message_body = "Sample test python mail"
 
message.attach(MIMEText(message_body, 'plain'))
filename=input("Enter the file name")
fileloc = input("Enter Attachment File location with file name and extension")
attachment = open(fileloc, "rb")
 
link = MIMEBase('application', 'octet-stream')
link.set_payload((attachment).read())
encoders.encode_base64(part)
link.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
message.attach(link)
smtp=input("Enter the smtp link through which you would like to send the mail") 
server = smtplib.SMTP(smtp, 587)
server.starttls()
password=input("Enter your password")
server.login(fromaddr, password)
text = message.as_string()
server.sendmail(fromadr, toadr, text)
server.quit()
