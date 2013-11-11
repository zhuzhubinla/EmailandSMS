import email
import mimetypes
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.MIMEMultipart import MIMEMultipart
import smtplib
import time

class sendEmailTask():
    def __init__(self):
        self.smtp=None

    def createConnect(self):
        print('Creating connect...')
        try:
            self.smtp=smtplib.SMTP_SSL()
            self.smtp.connect('smtp.gmail.com',465)
            self.smtp.login('binbinzhutest@gmail.com','zhuzhubin123')
            #smtp.sendmail(mail_from,mail_to,msg.as_string())
            #smtp.quit()
            print 'Creating connect ok...'
        except Exception,e:
            print e

        return self.smtp
    
    def sendTask(self,smtp):
        print 'Send one email at time:%s'%(time.strftime('%Y-%m-%d:%H:%M:%S',time.localtime(time.time())))
        mail_body='test message'
        mail_from='binbinzhutest@gmail.com'
        mail_to=['allenbintestzhu@gmail.com']
        msg=MIMEText(mail_body)
        msg['Subject']='test email'
        msg['To']=';'.join(mail_to)
        msg['date']=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        smtp.sendmail(mail_from,mail_to,msg.as_string())
       
        
    def logout(self,smtp):
        print 'Logout at time %s'%(time.strftime('%Y-%m-%d:%H:%M:%S',time.localtime(time.time())))
        smtp.quit()
        
    def getSmtp(self):
        return self.smtp
    
    
    