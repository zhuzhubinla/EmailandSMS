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
    emailTask=''
    file_list=[]
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(473, 334)
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
        self.line.setGeometry(QtCore.QRect(179, 10, 51, 321))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(220, 50, 81, 31))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(220, 90, 71, 21))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.loginStatus = QtGui.QLabel(Dialog)
        self.loginStatus.setGeometry(QtCore.QRect(100, 150, 54, 12))
        self.loginStatus.setObjectName(_fromUtf8("loginStatus"))
        self.pushButtonSend = QtGui.QPushButton(Dialog)
        self.pushButtonSend.setGeometry(QtCore.QRect(390, 220, 75, 23))
        self.pushButtonSend.setObjectName(_fromUtf8("pushButtonSend"))

        self.retranslateUi(Dialog)
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
        self.checkBox.setText(_translate("Dialog", "PNG", None))
        self.checkBox_2.setText(_translate("Dialog", "JPG", None))
        self.label_3.setText(_translate("Dialog", "Login Status:", None))
        self.loginStatus.setText(_translate("Dialog", "None", None))
        self.pushButtonSend.setText(_translate("Dialog", "Send", None))
        
    def doLogin(self):
        userName=self.userNamelineEdit.text()
        userPassword=self.userPasswordlineEdit.text()
        self.emailTask=sendEmailTask(userName,userPassword)
        self.emailTask.createConnect()
        self.loginStatus.setText(_translate("Dialog", self.emailTask.getLoginStatus(), None))
        
    def doLogout(self):
        self.emailTask.logout()
        
        
    def doSendEmail(self):
        self.getCheckBoxStatus()
        if self.checkBox_2.isChecked():
             self.emailTask.sendTask()
    
    def getCheckBoxStatus(self):
        if self.checkBox_2.isChecked():
            file_list.append('E:/new/a.png')
        if len(self.file_list)==0:
            QtGui.QMessageBox.information(self,"Message", "Please select one option?",QMessageBox.Ok)

        


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

