# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectFolderWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(404, 301)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.selectDirEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.selectDirEdit.setObjectName("selectDirEdit")
        self.horizontalLayout.addWidget(self.selectDirEdit)
        self.SelectDirButton = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        self.SelectDirButton.setObjectName("SelectDirButton")
        self.horizontalLayout.addWidget(self.SelectDirButton)

        self.retranslateUi(Form)
        self.SelectDirButton.clicked.connect(Form.selectDirLisener)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Start Directory: "))
        self.SelectDirButton.setText(_translate("Form", "..."))

