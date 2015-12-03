# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        Dialog.resize(400, 300)
        self.errorin = QtGui.QTextEdit(Dialog)
        self.errorin.setGeometry(QtCore.QRect(63, 50, 281, 161))
        self.errorin.setObjectName(_fromUtf8("errorin"))
        self.submit = QtGui.QPushButton(Dialog)
        self.submit.setGeometry(QtCore.QRect(60, 230, 98, 27))
        self.submit.setObjectName(_fromUtf8("submit"))
        self.cancel = QtGui.QPushButton(Dialog)
        self.cancel.setGeometry(QtCore.QRect(240, 230, 98, 27))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 9, 271, 31))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Error log", None))
        self.submit.setText(_translate("Dialog", "Submit", None))
        self.cancel.setText(_translate("Dialog", "Cancel", None))
        self.label.setText(_translate("Dialog", "Descreva o problema com LXXX", None))

