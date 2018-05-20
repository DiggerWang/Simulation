# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainFrame.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import Coin_Experiment
import GUI_Queue

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(628, 424)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 200, 141, 81))
        font = QtGui.QFont()
        font.setFamily("Hannotate SC")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 200, 141, 81))
        font = QtGui.QFont()
        font.setFamily("Hannotate SC")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 200, 141, 81))
        font = QtGui.QFont()
        font.setFamily("Hannotate SC")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 30, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(220, 100, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 设置按钮监听器
        self.pushButton.clicked.connect(self.on_click_1)
        self.pushButton_2.clicked.connect(self.on_click_2)
        self.pushButton_3.clicked.connect(self.on_click_3)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Coin\n"
                                                   "Experiment"))
        self.pushButton_2.setText(_translate("Form", "Queueing\n"
                                                     "Experiment"))
        self.pushButton_3.setText(_translate("Form", "Inventory\n"
                                                     "Experiment"))
        self.label.setText(_translate("Form", "Model Stimulation"))
        self.label_2.setText(_translate("Form", "WangHao,XuMingHai"))

    def on_click_1(self):
        os.system("python Coin_Experiment.py")

    def on_click_2(self):
        os.system("python GUI_Queue.py")

    def on_click_3(self):
        os.system("python GUI_Inventory.py")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
