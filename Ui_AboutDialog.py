# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboout_dialog.ui'
#
# Created: Mon May  6 09:50:42 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

import os
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
    
PATH = os.path.realpath(__file__).replace('Ui_AboutDialog.py', '')

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName(_fromUtf8("AboutDialog"))
        AboutDialog.setWindowModality(QtCore.Qt.WindowModal)
        AboutDialog.resize(443, 300)
        AboutDialog.setMinimumSize(QtCore.QSize(443, 300))
        AboutDialog.setMaximumSize(QtCore.QSize(443, 300))
        AboutDialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        AboutDialog.setSizeGripEnabled(True)
        AboutDialog.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(AboutDialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.applicationLogo = QtGui.QLabel(AboutDialog)
        self.applicationLogo.setGeometry(QtCore.QRect(10, 10, 131, 141))
        self.applicationLogo.setText(_fromUtf8(""))
        self.applicationLogo.setTextFormat(QtCore.Qt.PlainText)
        self.applicationLogo.setPixmap(QtGui.QPixmap(_fromUtf8(os.path.join(PATH, "data/exfmplayer128.png"))))
        self.applicationLogo.setObjectName(_fromUtf8("applicationLogo"))
        self.applicationName = QtGui.QLabel(AboutDialog)
        self.applicationName.setGeometry(QtCore.QRect(170, 20, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.applicationName.setFont(font)
        self.applicationName.setObjectName(_fromUtf8("applicationName"))
        self.applicationComment = QtGui.QLabel(AboutDialog)
        self.applicationComment.setGeometry(QtCore.QRect(170, 60, 251, 71))
        self.applicationComment.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.applicationComment.setWordWrap(True)
        self.applicationComment.setObjectName(_fromUtf8("applicationComment"))
        self.label_4 = QtGui.QLabel(AboutDialog)
        self.label_4.setGeometry(QtCore.QRect(170, 150, 61, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.applicationAuthor = QtGui.QLabel(AboutDialog)
        self.applicationAuthor.setGeometry(QtCore.QRect(240, 150, 171, 16))
        self.applicationAuthor.setObjectName(_fromUtf8("applicationAuthor"))
        self.label_6 = QtGui.QLabel(AboutDialog)
        self.label_6.setGeometry(QtCore.QRect(170, 170, 57, 14))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.applicationLicense = QtGui.QLabel(AboutDialog)
        self.applicationLicense.setGeometry(QtCore.QRect(240, 170, 171, 16))
        self.applicationLicense.setObjectName(_fromUtf8("applicationLicense"))
        self.label_8 = QtGui.QLabel(AboutDialog)
        self.label_8.setGeometry(QtCore.QRect(170, 190, 57, 14))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.applicationYear = QtGui.QLabel(AboutDialog)
        self.applicationYear.setGeometry(QtCore.QRect(240, 190, 57, 14))
        self.applicationYear.setObjectName(_fromUtf8("applicationYear"))

        self.retranslateUi(AboutDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AboutDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(_translate("AboutDialog", "Dialog", None))
        self.applicationName.setText(_translate("AboutDialog", "Application Name <Version>", None))
        self.applicationComment.setText(_translate("AboutDialog", "Comment", None))
        self.label_4.setText(_translate("AboutDialog", "Author:", None))
        self.applicationAuthor.setText(_translate("AboutDialog", "Vladimir Kolev", None))
        self.label_6.setText(_translate("AboutDialog", "License:", None))
        self.applicationLicense.setText(_translate("AboutDialog", "Apache MIT License", None))
        self.label_8.setText(_translate("AboutDialog", "Year:", None))
        self.applicationYear.setText(_translate("AboutDialog", "2013", None))

