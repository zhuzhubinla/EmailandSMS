import email
import mimetypes
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.MIMEMultipart import MIMEMultipart
import smtplib
import time

class sendEmailTask():
    def __init__(self,userName,passWord):
        self.smtp=None
        self.userName=userName
        self.passWord=passWord
        self.loginStatus=None

    def createConnect(self):
        print('Creating connect...')
        try:
            self.smtp=smtplib.SMTP_SSL()
            self.smtp.connect('smtp.gmail.com',465)
            self.smtp.login(self.userName,self.passWord)
            #smtp.sendmail(mail_from,mail_to,msg.as_string())
            #smtp.quit()
            print 'Creating connect ok...'
            self.loginStatus='OK'
        except Exception,e:
            print e
            self.loginStatus='False'

        return self.smtp
    
    def sendTask(self):
        print 'Send one email at time:%s'%(time.strftime('%Y-%m-%d:%H:%M:%S',time.localtime(time.time())))
        #mail_body='test message'
        #mail_to=['allenbintestzhu@gmail.com']
        #msg['Subject']='test email'
        #msg['To']=';'.join(mail_to)
        #msg['date']=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        #self.smtp.sendmail(mail_from,mail_to,msg.as_string())
        
        mail_body='Send a png picture from gmail'
        mail_from='allenbintestzhu@gmail.com'
        mail_to=['zhu.zhubinlala@gmail.com']
        msg=MIMEMultipart()
        msg['Subject']='test email'
        msg['To']=';'.join(mail_to)
        msg['date']=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        txt=MIMEText('test message')
        msg.attach(txt)
        picPath=['./res/a.jpg']
        for img in picPath:
            pic=open(img,'rb')
            readPic=MIMEImage(pic.read())
            msg.attach(readPic)
            
        self.smtp.sendmail(mail_from,mail_to,msg.as_string())

       
        
    def logout(self):
        print 'Logout at time %s'%(time.strftime('%Y-%m-%d:%H:%M:%S',time.localtime(time.time())))
        self.smtp.quit()
        
    def getSmtp(self):
        return self.smtp
    
    def getLoginStatus(self):
        return self.loginStatus
    
    
    