# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowForm.py'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from SelectFolderWindow import Ui_Form
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys

class QtWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(QtWindow, self).__init__()
        self.setupUi(self)

    def selectDirLisener(self):
        filename = QFileDialog.getExistingDirectory(self, u"选择需要的文件夹", u'C:/')
        lineEdit = self.findChild(QtWidgets.QLineEdit, "selectDirEdit")
        lineEdit.setText(filename)

app = QtWidgets.QApplication(sys.argv)
window = QtWindow()
window.show()
sys.exit(app.exec_())
