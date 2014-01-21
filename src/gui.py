# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a.ui'
#
# Created: Fri Jan 03 14:34:04 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from sendEmail import sendEmailTask
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(QtGui.QWidget):
    emailTask=None
    image_file=[]
    audio_file=[]
    video_file=[]
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(699, 402)
        self.pushButtonLogout = QtGui.QPushButton(Dialog)
        self.pushButtonLogout.setGeometry(QtCore.QRect(90, 180, 51, 23))
        self.pushButtonLogout.setObjectName(_fromUtf8("pushButtonLogout"))
        self.pushButtonLogin = QtGui.QPushButton(Dialog)
        self.pushButtonLogin.setGeometry(QtCore.QRect(10, 180, 51, 23))
        self.pushButtonLogin.setObjectName(_fromUtf8("pushButtonLogin"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 70, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.userNamelineEdit = QtGui.QLineEdit(Dialog)
        self.userNamelineEdit.setGeometry(QtCore.QRect(70, 70, 113, 20))
        self.userNamelineEdit.setObjectName(_fromUtf8("userNamelineEdit"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.userPasswordlineEdit = QtGui.QLineEdit(Dialog)
        self.userPasswordlineEdit.setGeometry(QtCore.QRect(70, 110, 113, 20))
        self.userPasswordlineEdit.setObjectName(_fromUtf8("userPasswordlineEdit"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(170, 10, 51, 420))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.loginStatus = QtGui.QLabel(Dialog)
        self.loginStatus.setGeometry(QtCore.QRect(100, 150, 54, 12))
        self.loginStatus.setObjectName(_fromUtf8("loginStatus"))
        self.pushButtonSend = QtGui.QPushButton(Dialog)
        self.pushButtonSend.setGeometry(QtCore.QRect(390, 220, 75, 23))
        self.pushButtonSend.setObjectName(_fromUtf8("pushButtonSend"))
        self.checkBox_Gif = QtGui.QCheckBox(Dialog)
        self.checkBox_Gif.setGeometry(QtCore.QRect(200, 40, 71, 16))
        self.checkBox_Gif.setObjectName(_fromUtf8("checkBox_Gif"))
        self.checkBox_BMP = QtGui.QCheckBox(Dialog)
        self.checkBox_BMP.setGeometry(QtCore.QRect(200, 70, 71, 16))
        self.checkBox_BMP.setObjectName(_fromUtf8("checkBox_BMP"))
        self.checkBox_WBMP = QtGui.QCheckBox(Dialog)
        self.checkBox_WBMP.setGeometry(QtCore.QRect(200, 100, 71, 16))
        self.checkBox_WBMP.setObjectName(_fromUtf8("checkBoxWBMP"))
        self.checkBox_MP3 = QtGui.QCheckBox(Dialog)
        self.checkBox_MP3.setGeometry(QtCore.QRect(280, 250, 71, 16))
        self.checkBox_MP3.setObjectName(_fromUtf8("checkBox_MP3"))
        self.checkBox_MID = QtGui.QCheckBox(Dialog)
        self.checkBox_MID.setGeometry(QtCore.QRect(280, 40, 71, 16))
        self.checkBox_MID.setObjectName(_fromUtf8("checkBox_MID"))
        self.checkBox_WMA = QtGui.QCheckBox(Dialog)
        self.checkBox_WMA.setGeometry(QtCore.QRect(280, 70, 71, 16))
        self.checkBox_WMA.setObjectName(_fromUtf8("checkBox_WMA"))
        self.checkBox_WAV = QtGui.QCheckBox(Dialog)
        self.checkBox_WAV.setGeometry(QtCore.QRect(280, 100, 71, 16))
        self.checkBox_WAV.setObjectName(_fromUtf8("checkBox_WAV"))
        self.checkBox_AAC = QtGui.QCheckBox(Dialog)
        self.checkBox_AAC.setGeometry(QtCore.QRect(280, 130, 71, 16))
        self.checkBox_AAC.setObjectName(_fromUtf8("checkBox_AAC"))
        self.checkBox_IMY = QtGui.QCheckBox(Dialog)
        self.checkBox_IMY.setGeometry(QtCore.QRect(280, 160, 71, 16))
        self.checkBox_IMY.setObjectName(_fromUtf8("checkBox_IMY"))
        self.checkBox_EAAC = QtGui.QCheckBox(Dialog)
        self.checkBox_EAAC.setGeometry(QtCore.QRect(280, 190, 71, 16))
        self.checkBox_EAAC.setObjectName(_fromUtf8("checkBox_EAAC"))
        self.checkBox_EAAC1 = QtGui.QCheckBox(Dialog)
        self.checkBox_EAAC1.setGeometry(QtCore.QRect(280, 220, 71, 16))
        self.checkBox_EAAC1.setObjectName(_fromUtf8("checkBox_EAAC1"))
        self.checkBox_H263_AAC = QtGui.QCheckBox(Dialog)
        self.checkBox_H263_AAC.setGeometry(QtCore.QRect(370, 160, 71, 16))
        self.checkBox_H263_AAC.setObjectName(_fromUtf8("checkBox_H263_AAC"))
        self.checkBox_H263_AMR = QtGui.QCheckBox(Dialog)
        self.checkBox_H263_AMR.setGeometry(QtCore.QRect(370, 40, 71, 16))
        self.checkBox_H263_AMR.setObjectName(_fromUtf8("checkBox_H263_AMR"))
        self.checkBox_H263_MP3 = QtGui.QCheckBox(Dialog)
        self.checkBox_H263_MP3.setGeometry(QtCore.QRect(370, 70, 71, 16))
        self.checkBox_H263_MP3.setObjectName(_fromUtf8("checkBox_H263_MP3"))
        self.checkBox_H263_QCELP = QtGui.QCheckBox(Dialog)
        self.checkBox_H263_QCELP.setGeometry(QtCore.QRect(370, 100, 71, 16))
        self.checkBox_H263_QCELP.setObjectName(_fromUtf8("checkBox_H263_QCELP"))
        self.checkBox_H263_SQCP = QtGui.QCheckBox(Dialog)
        self.checkBox_H263_SQCP.setGeometry(QtCore.QRect(370, 130, 71, 16))
        self.checkBox_H263_SQCP.setObjectName(_fromUtf8("checkBox_H263_SQCP"))
        self.checkBox_H264_MP3 = QtGui.QCheckBox(Dialog)
        self.checkBox_H264_MP3.setGeometry(QtCore.QRect(470, 100, 71, 16))
        self.checkBox_H264_MP3.setObjectName(_fromUtf8("checkBox_H264_MP3"))
        self.checkBox_H264_AAC = QtGui.QCheckBox(Dialog)
        self.checkBox_H264_AAC.setGeometry(QtCore.QRect(470, 40, 71, 16))
        self.checkBox_H264_AAC.setObjectName(_fromUtf8("checkBox_H264_AAC"))
        self.checkBox_H264_AMR = QtGui.QCheckBox(Dialog)
        self.checkBox_H264_AMR.setGeometry(QtCore.QRect(470, 70, 71, 16))
        self.checkBox_H264_AMR.setObjectName(_fromUtf8("checkBox_H264_AMR"))
        self.checkBox_H264_QCELP = QtGui.QCheckBox(Dialog)
        self.checkBox_H264_QCELP.setGeometry(QtCore.QRect(470, 130, 81, 16))
        self.checkBox_H264_QCELP.setObjectName(_fromUtf8("checkBox_H264_QCELP"))
        self.checkBox_H264_SQCP = QtGui.QCheckBox(Dialog)
        self.checkBox_H264_SQCP.setGeometry(QtCore.QRect(470, 160, 81, 16))
        self.checkBox_H264_SQCP.setObjectName(_fromUtf8("checkBox_H264_SQCP"))
        self.checkBox_MP_AAC = QtGui.QCheckBox(Dialog)
        self.checkBox_MP_AAC.setGeometry(QtCore.QRect(580, 40, 101, 16))
        self.checkBox_MP_AAC.setObjectName(_fromUtf8("checkBox_MP_AAC"))
        self.checkBox_MP_AMR = QtGui.QCheckBox(Dialog)
        self.checkBox_MP_AMR.setGeometry(QtCore.QRect(580, 66, 91, 20))
        self.checkBox_MP_AMR.setObjectName(_fromUtf8("checkBox_MP_AMR"))
        self.checkBox_MP_MP3 = QtGui.QCheckBox(Dialog)
        self.checkBox_MP_MP3.setGeometry(QtCore.QRect(580, 100, 91, 16))
        self.checkBox_MP_MP3.setObjectName(_fromUtf8("checkBox_MP_MP3"))
        self.checkBox_MP_QCELP = QtGui.QCheckBox(Dialog)
        self.checkBox_MP_QCELP.setGeometry(QtCore.QRect(580, 130, 101, 16))
        self.checkBox_MP_QCELP.setObjectName(_fromUtf8("checkBox_MP_QCELP"))
        self.checkBox_MP_SQCP = QtGui.QCheckBox(Dialog)
        self.checkBox_MP_SQCP.setGeometry(QtCore.QRect(580, 160, 101, 16))
        self.checkBox_MP_SQCP.setObjectName(_fromUtf8("checkBox_MP_SQCP"))
        self.checkBox_JPG = QtGui.QCheckBox(Dialog)
        self.checkBox_JPG.setGeometry(QtCore.QRect(200, 130, 71, 16))
        self.checkBox_JPG.setObjectName(_fromUtf8("checkBox_JPG"))
        self.checkBox_PNG = QtGui.QCheckBox(Dialog)
        self.checkBox_PNG.setGeometry(QtCore.QRect(200, 160, 71, 16))
        self.checkBox_PNG.setObjectName(_fromUtf8("checkBox_PNG"))
        
        
        

        self.retranslateUi(Dialog)
        self.fillEmailAddress()
        QtCore.QObject.connect(self.pushButtonLogin, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doLogin)
        QtCore.QObject.connect(self.pushButtonLogout, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doLogout)
        QtCore.QObject.connect(self.pushButtonSend, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doSendEmail)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
       
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "EmailSender", None))
        self.pushButtonLogout.setText(_translate("Dialog", "Logout", None))
        self.pushButtonLogin.setText(_translate("Dialog", "Login", None))
        self.label.setText(_translate("Dialog", "Username:", None))
        self.label_2.setText(_translate("Dialog", "Password", None))
        self.label_3.setText(_translate("Dialog", "Login Status:", None))
        self.loginStatus.setText(_translate("Dialog", "None", None))
        self.pushButtonSend.setText(_translate("Dialog", "Send", None))
        self.checkBox_Gif.setText(_translate("Dialog", "Gif", None))
        self.checkBox_BMP.setText(_translate("Dialog", "BMP", None))
        self.checkBox_WBMP.setText(_translate("Dialog", "WBMP", None))
        self.checkBox_MP3.setText(_translate("Dialog", "MP3", None))
        self.checkBox_MID.setText(_translate("Dialog", "MID", None))
        self.checkBox_WMA.setText(_translate("Dialog", "WMA", None))
        self.checkBox_WAV.setText(_translate("Dialog", "WAV", None))
        self.checkBox_AAC.setText(_translate("Dialog", "AAC", None))
        self.checkBox_IMY.setText(_translate("Dialog", "IMY", None))
        self.checkBox_EAAC.setText(_translate("Dialog", "EAAC", None))
        self.checkBox_EAAC1.setText(_translate("Dialog", "EAAC+", None))
        self.checkBox_H263_AAC.setText(_translate("Dialog", "H263_AAC", None))
        self.checkBox_H263_AMR.setText(_translate("Dialog", "H263_AMR", None))
        self.checkBox_H263_MP3.setText(_translate("Dialog", "H263_MP3", None))
        self.checkBox_H263_QCELP.setText(_translate("Dialog", "H263_QCELP", None))
        self.checkBox_H263_SQCP.setText(_translate("Dialog", "H263_SQCP", None))
        self.checkBox_H264_MP3.setText(_translate("Dialog", "H264_MP3", None))
        self.checkBox_H264_AAC.setText(_translate("Dialog", "H264_AAC", None))
        self.checkBox_H264_AMR.setText(_translate("Dialog", "H264_AMR", None))
        self.checkBox_H264_QCELP.setText(_translate("Dialog", "H264_QCELP", None))
        self.checkBox_H264_SQCP.setText(_translate("Dialog", "H264_SQCP", None))
        self.checkBox_MP_AAC.setText(_translate("Dialog", "MPEG-4_AAC", None))
        self.checkBox_MP_AMR.setText(_translate("Dialog", "MPEG-4_AMR", None))
        self.checkBox_MP_MP3.setText(_translate("Dialog", "MPEG-4_MP3", None))
        self.checkBox_MP_QCELP.setText(_translate("Dialog", "MPEG-4_QCELP", None))
        self.checkBox_MP_SQCP.setText(_translate("Dialog", "MPEG-4_SQCP", None))
        self.checkBox_JPG.setText(_translate("Dialog", "JPG", None))
        self.checkBox_PNG.setText(_translate("Dialog", "PNG", None))
        
        
    def fillEmailAddress(self):
        emailAccountFile=open('./res/a.txt','r')
        emailAccount=emailAccountFile.read().split(',')
        eamailAddress=emailAccount[0]
        emailPassword=emailAccount[1]
        self.userNamelineEdit.setText(eamailAddress)
        self.userPasswordlineEdit.setText(emailPassword)
        
    def doLogin(self):
        userName=self.userNamelineEdit.text()
        userPassword=self.userPasswordlineEdit.text()
        self.emailTask=sendEmailTask(userName,userPassword)
        self.emailTask.createConnect()
        self.loginStatus.setText(_translate("Dialog", self.emailTask.getLoginStatus(), None))
        
    def doLogout(self):
        self.emailTask.logout()
        self.emailTask=None
        
        
    def doSendEmail(self):
        if self.emailTask!= None:
            self.getCheckBoxStatus()
            if len(self.image_file)==0 and len(self.audio_file)==0 and len(self.video_file)==0:
                QtGui.QMessageBox.information(self,"Message", "Please select one option?",QMessageBox.Ok)
            else:
                if len(self.image_file)!=0:
                    self.emailTask.sendImage(self.image_file)
                    self.image_file=[]
                if len(self.audio_file)!=0:
                    self.emailTask.sendAudio(self.audio_file)
                    self.audio_file=[]
                if len(self.video_file)!=0:
                    self.emailTask.sendTask(self.video_file)
                    self.video_file=[]  
        else:
            QtGui.QMessageBox.information(self,"Notification", "Please login?",QMessageBox.Ok)
        
    
    def getCheckBoxStatus(self):
        if self.checkBox_PNG.isChecked():
            self.image_file.append('./res/image/PNG_1024x769.png')
        if self.checkBox_JPG.isChecked():
             self.image_file.append('。/res/image/JPG.jpg')
        if self.checkBox_BMP.isChecked():
            self.image_file.append('./res/image/WBMP_640x480.bmp')
        if self.checkBox_Gif.isChecked():
            self.image_file.append('./res/image/WBMP_640x480.bmp')
        if self.checkBox_WBMP.isChecked():
            self.image_file.append('./res/image/WBMP_640x480.bmp')
            
        if self.checkBox_AAC.isChecked():
            self.audio_file.append('./res/audio/mono_filename_48Khz_16Bit_8Kbps.aac')
        if self.checkBox_EAAC.isChecked():
            self.audio_file.append('./res/audio/PNG_1024x769.png')
        if self.checkBox_EAAC1.isChecked():
            self.audio_file.append('./res/audio/PNG_1024x769.png')
        if self.checkBox_IMY.isChecked():
            self.audio_file.append('./res/audioPNG_1024x769.png')
        if self.checkBox_MID.isChecked():
            self.audio_file.append('./res/audio/PNG_1024x769.png')
        if self.checkBox_MP3.isChecked():
            self.audio_file.append('./res/audio/mp3.mp3')
        if self.checkBox_WAV.isChecked():
            self.audio_file.append('./res/audio/PNG_1024x769.png')
        if self.checkBox_WMA.isChecked():
            self.audio_file.append('./res/audio/PNG_1024x769.png')
        if self.checkBox_EAAC1.isChecked():
            self.audio_file.append('./res/audio/PNG_1024x769.png')
            
            
        if self.checkBox_H263_AAC.isChecked():
            self.audio_file.append('./res/video/h263PNG_1024x769.png')
        if self.checkBox_H263_AMR.isChecked():
            self.audio_file.append('./res/video/h263/PNG_1024x769.png')
        if self.checkBox_H263_MP3.isChecked():
            self.audio_file.append('./res/video/h263/PNG_1024x769.png')
        if self.checkBox_H263_QCELP.isChecked():
            self.audio_file.append('./res/video/h263/PNG_1024x769.png')
        if self.checkBox_H263_SQCP.isChecked():
            self.audio_file.append('./res/video/h263/PNG_1024x769.png')
        
        if self.checkBox_H264_AAC.isChecked():
            self.file_list.append('./res/video/h264/PNG_1024x769.png')
        if self.checkBox_H264_AMR.isChecked():
            self.file_list.append('./res/video/h264/PNG_1024x769.png')
        if self.checkBox_H264_MP3.isChecked():
            self.file_list.append('./res/video/h264/PNG_1024x769.png')
        if self.checkBox_H264_QCELP.isChecked():
            self.file_list.append('./res/video/h264/PNG_1024x769.png')
        if self.checkBox_H264_SQCP.isChecked():
            self.file_list.append('./res/video/h264/PNG_1024x769.png')
            
        if self.checkBox_MP_AAC.isChecked():
            self.video_file.append('./res/video/mp4/PNG_1024x769.png')
        if self.checkBox_MP_AMR.isChecked():
            self.video_file.append('./res/video/mp4/PNG_1024x769.png')
        if self.checkBox_MP_MP3.isChecked():
            self.video_file.append('./res/video/mp4/PNG_1024x769.png')
        if self.checkBox_MP_QCELP.isChecked():
            self.video_file.append('./res/video/mp4/PNG_1024x769.png')
        if self.checkBox_MP_SQCP.isChecked():
            self.video_file.append('./res/video/mp4/PNG_1024x769.png')
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

