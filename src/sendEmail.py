import email
import mimetypes
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.MIMEAudio import MIMEAudio
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email import Encoders
import smtplib
import time
import os
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
    
    def sendImage(self,filePath):
        print 'Send one email at time:%s'%(time.strftime('%Y-%m-%d:%H:%M:%S',time.localtime(time.time())))
        #mail_body='test message'
        #mail_to=['allenbintestzhu@gmail.com']
        #msg['Subject']='test email'
        #msg['To']=';'.join(mail_to)
        #msg['date']=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        #self.smtp.sendmail(mail_from,mail_to,msg.as_string())
        self.filePath=filePath
        mail_body='Send a png picture from gmail'
        mail_from='allenbintestzhu@gmail.com'
        mail_to=['zhu.zhubinlala@gmail.com']
        msg=MIMEMultipart()
        msg['Subject']='test email'
        msg['To']=';'.join(mail_to)
        msg['date']=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        txt=MIMEText('test message')
        msg.attach(txt)
        for img in filePath:
            print os.getcwd()
            pic=open(img,'rb')
            readPic=MIMEImage(pic.read())
            msg.attach(readPic)
            self.smtp.sendmail(mail_from,mail_to,msg.as_string())
            
    def sendAudio(self,audioFilePath):
        self.audioFilePath=audioFilePath
        mail_body='Send a png picture from gmail'
        mail_from='allenbintestzhu@gmail.com'
        mail_to=['zhu.zhubinlala@gmail.com']
        msg=MIMEMultipart()
        msg['Subject']='test email'
        msg['To']=';'.join(mail_to)
        msg['date']=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        txt=MIMEText('test message')
        msg.attach(txt)
        for audioFile in audioFilePath:
            print os.getcwd()
            audioFileBit=open(audioFile,'rb')
            audioFileRead=MIMEAudio(audioFileBit.read())
            audioFileRead.add_header('Content-Disposition', 'attachment; filename="ddd"')
            msg.attach(audioFileRead)
            self.smtp.sendmail(mail_from,mail_to,msg.as_string())
    
    def sendVideoFile(self,videoFilePath):
        self.videoFilePath=videoFilePath
        mail_body='Send a png picture from gmail'
        mail_from='allenbintestzhu@gmail.com'
        mail_to=['zhu.zhubinlala@gmail.com']
        msg=MIMEMultipart()
        msg['Subject']='test email'
        msg['To']=';'.join(mail_to)
        msg['date']=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        txt=MIMEText('test message')
        msg.attach(txt)
        for videoFile in videoFilePath:
            videofFileMIME=MIMEBase('application', 'octet-stream')
            videofFileMIME.set_payload(open(videoFile,'rb').read())
            Encoders.encode_base64(videofFileMIME)
            videofFileMIME.add_header('Content-Disposition', 'attachment; filename="%s"'%os.path.basename(videoFile))
            msg.attach(videofFileMIME)
            self.smtp.sendmail(mail_from,mail_to,msg.as_string())
            videoFileBit.close()
            time.sleep(10)
        

       
        
    def logout(self):
        print 'Logout at time %s'%(time.strftime('%Y-%m-%d:%H:%M:%S',time.localtime(time.time())))
        self.smtp.quit()
        
    def getSmtp(self):
        return self.smtp
    
    def getLoginStatus(self):
        return self.loginStatus
    
    
    