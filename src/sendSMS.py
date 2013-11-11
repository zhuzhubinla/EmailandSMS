from PyFetion import *


class sendSMSTask():
    def __init__(self):
        self.smsConnection=None
    
    def login(self,phoneNumber,passWord):
        print 'SMS login...'
        self.smsConnection=PyFetion(phoneNumber,passWord,'TCP',debug=False)
        self.smsConnection.login(FetionOnline)
        
    def sendSMS(self,message):
        print 'Sending sms ...'
        self.smsConnection.send_sms(message)
        
    def logout(self):
        print 'SMS logout...'
        self.smsConnection.logout()