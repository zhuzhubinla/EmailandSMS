# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a.ui'
#
# Created: Fri Jan 03 14:34:04 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(473, 334)
        self.pushButtonLogout = QtGui.QPushButton(Dialog)
        self.pushButtonLogout.setGeometry(QtCore.QRect(100, 170, 51, 23))
        self.pushButtonLogout.setObjectName(_fromUtf8("pushButtonLogout"))
        self.pushButtonLogin = QtGui.QPushButton(Dialog)
        self.pushButtonLogin.setGeometry(QtCore.QRect(30, 170, 51, 23))
        self.pushButtonLogin.setObjectName(_fromUtf8("pushButtonLogin"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 70, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 70, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 110, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButtonLogout.setText(_translate("Dialog", "Logout", None))
        self.pushButtonLogin.setText(_translate("Dialog", "Login", None))
        self.label.setText(_translate("Dialog", "Username:", None))
        self.label_2.setText(_translate("Dialog", "Password", None))
        self.checkBox.setText(_translate("Dialog", "PNG", None))
        self.checkBox_2.setText(_translate("Dialog", "JPG", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

