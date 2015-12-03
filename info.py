# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
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
        Dialog.resize(384, 181)
        self.msg = QtGui.QLabel(Dialog)
        self.msg.setGeometry(QtCore.QRect(10, 20, 361, 111))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg.sizePolicy().hasHeightForWidth())
        self.msg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Vemana2000"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.msg.setFont(font)
        self.msg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.msg.setTextFormat(QtCore.Qt.AutoText)
        self.msg.setScaledContents(False)
        self.msg.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.msg.setIndent(0)
        self.msg.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard)
        self.msg.setObjectName(_fromUtf8("msg"))
        self.ok = QtGui.QPushButton(Dialog)
        self.ok.setGeometry(QtCore.QRect(140, 140, 98, 27))
        self.ok.setObjectName(_fromUtf8("ok"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Info", None))
        self.msg.setText(_translate("Dialog", "Ola Marilene ", None))
        self.ok.setText(_translate("Dialog", "OK", None))

