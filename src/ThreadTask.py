import threading
import time
from sendEmail import sendEmailTask
from sendSMS import sendSMSTask

class threadTask(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop=False
    
    def run(self):
        send_task=sendEmailTask()
        send_sms_task=sendSMSTask()
        while not self.stop:
            send_sms_task.login('13518171925','******')
            send_sms_task.sendSMS('test')
            send_sms_task.logout()
            gmail_smtp=send_task.createConnect()
            send_task.sendtask(gmail_smtp) 
            time.sleep(10)
            send_task.logout(gmail_smtp)
            time.sleep(60*10)
            
            
    def stop(self):
        self.stop=True
