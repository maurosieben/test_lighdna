# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testing.ui'
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
        Dialog.resize(290, 229)
        self.msg = QtGui.QLabel(Dialog)
        self.msg.setGeometry(QtCore.QRect(30, 30, 311, 31))
        self.msg.setObjectName(_fromUtf8("msg"))
        self.start = QtGui.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(90, 90, 98, 27))
        self.start.setObjectName(_fromUtf8("start"))
        self.bk = QtGui.QPushButton(Dialog)
        self.bk.setGeometry(QtCore.QRect(20, 130, 61, 27))
        self.bk.setObjectName(_fromUtf8("bk"))
        self.fw = QtGui.QPushButton(Dialog)
        self.fw.setGeometry(QtCore.QRect(200, 130, 61, 27))
        self.fw.setObjectName(_fromUtf8("fw"))
        self.stop = QtGui.QPushButton(Dialog)
        self.stop.setGeometry(QtCore.QRect(90, 170, 98, 27))
        self.stop.setObjectName(_fromUtf8("stop"))
        self.play = QtGui.QPushButton(Dialog)
        self.play.setGeometry(QtCore.QRect(110, 130, 61, 27))
        self.play.setObjectName(_fromUtf8("play"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Teste LightDNA", None))
        self.msg.setText(_translate("Dialog", "Luminária LXXX  sendo testada", None))
        self.start.setText(_translate("Dialog", "Iniciar", None))
        self.bk.setText(_translate("Dialog", "<<", None))
        self.fw.setText(_translate("Dialog", ">>", None))
        self.stop.setText(_translate("Dialog", "Finalizar", None))
        self.play.setText(_translate("Dialog", "Play", None))

