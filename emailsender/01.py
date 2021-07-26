import smtplib

to = input("Enter the e-mail id of recipient:\n")
content=input("Enter the content for mail:\n")
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)  
    # gmail service uses 587 as port number
    server.ehlo()  #make the communication between the smtp server of gmail
    server.starttls()  #Start the session
    server.login('sendersemail@gmail.com','1234')    #login into gmail account using this command
    server.sendmail('senderemail@gmail.com',to,content)
    server.close()
sendEmail(to,content)

#cann't complete due to  2 step verification is on :)
