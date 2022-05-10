import smtplib as sm
#for having hidden password
from getpass import getpass

#imports related to structured emails
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

FROM_EMAIL = "ishwin899@gmail.com"
PASSWORD = getpass()
TO_EMAILS = ["ishwin9@gmail.com","ishwin900@gmail.com"]

#create connection with host

server = sm.SMTP(host = "smtp.gmail.com", port = 587)

print("CONNECTION CREATED WITH GMAIL")

#Enable security layers

server.starttls()

print("SECURITY LAYERS ENABLED")

#Login

server.login(FROM_EMAIL,PASSWORD)

print("LOGGED IN SUCCESSFULLY")

#compose email and send 

for to in TO_EMAILS:
       #constructing structured email
       mail = MIMEMultipart()
       mail['Subject'] = "Python testing email"
       mail['To'] = to
       msg = "this is testing email using python"
       
       attachable_text = MIMEText(msg,"plain")
       mail.attach(attachable_text)

       sendable_email = mail.as_string()

       server.sendmail(FROM_EMAIL,to,sendable_email)

print('EMAILS SENT')

#logout and destroy connection

server.quit()

print('LOGGED OUT AND KILLED THE CONNECTION')




