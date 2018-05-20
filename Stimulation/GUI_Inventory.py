# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Inventory.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import sys
import os
import pandas as pd
import time
import threading

class Ui_Form(object):
    def setupUi(self, Form):
        self.Cache_clear()
        Form.setObjectName("Form")
        Form.resize(1440, 900)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(30, 430, 611, 451))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 0, 611, 421))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 609, 419))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 611, 421))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(22)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 611, 421))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 609, 419))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 611, 421))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(8)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab, "")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(870, 20, 541, 861))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 521, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 470, 521, 391))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setGeometry(QtCore.QRect(0, 0, 511, 351))
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_23.setScaledContents(True)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.groupBox_12 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_12.setGeometry(QtCore.QRect(20, 320, 211, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setObjectName("groupBox_12")
        self.label_24 = QtWidgets.QLabel(self.groupBox_12)
        self.label_24.setGeometry(QtCore.QRect(10, 40, 131, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.groupBox_12)
        self.label_25.setGeometry(QtCore.QRect(10, 70, 41, 16))
        self.label_25.setObjectName("label_25")
        self.label_35 = QtWidgets.QLabel(self.groupBox_12)
        self.label_35.setGeometry(QtCore.QRect(120, 70, 21, 16))
        self.label_35.setObjectName("label_35")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox_12)
        self.lineEdit_18.setGeometry(QtCore.QRect(50, 70, 61, 21))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_12)
        self.lineEdit_19.setGeometry(QtCore.QRect(140, 70, 61, 21))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.groupBox_12)
        self.buttonBox.setGeometry(QtCore.QRect(20, 100, 164, 32))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_13.setGeometry(QtCore.QRect(310, 320, 211, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_13.setFont(font)
        self.groupBox_13.setObjectName("groupBox_13")
        self.label_36 = QtWidgets.QLabel(self.groupBox_13)
        self.label_36.setGeometry(QtCore.QRect(10, 40, 131, 16))
        self.label_36.setObjectName("label_36")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox_13)
        self.lineEdit_20.setGeometry(QtCore.QRect(50, 70, 61, 21))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox_13)
        self.lineEdit_21.setGeometry(QtCore.QRect(140, 70, 61, 21))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.groupBox_13)
        self.buttonBox_2.setGeometry(QtCore.QRect(20, 100, 164, 32))
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.label_37 = QtWidgets.QLabel(self.groupBox_13)
        self.label_37.setGeometry(QtCore.QRect(120, 70, 21, 16))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.groupBox_13)
        self.label_38.setGeometry(QtCore.QRect(10, 70, 41, 16))
        self.label_38.setObjectName("label_38")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(660, 430, 201, 451))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(20, 50, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_20 = QtWidgets.QLabel(self.groupBox_3)
        self.label_20.setGeometry(QtCore.QRect(90, 80, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 80, 61, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 80, 61, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(20, 130, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_16.setGeometry(QtCore.QRect(110, 160, 61, 21))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_17.setGeometry(QtCore.QRect(20, 160, 61, 21))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setGeometry(QtCore.QRect(90, 160, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.lcdNumber = QtWidgets.QLCDNumber(self.groupBox_3)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 390, 101, 30))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.setStyleSheet('background-color:gray')
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(20, 360, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.buttonBox_3 = QtWidgets.QDialogButtonBox(self.groupBox_3)
        self.buttonBox_3.setGeometry(QtCore.QRect(10, 210, 164, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonBox_3.setFont(font)
        self.buttonBox_3.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_3.setObjectName("buttonBox_3")
        self.label_40 = QtWidgets.QLabel(self.groupBox_3)
        self.label_40.setGeometry(QtCore.QRect(20, 270, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.groupBox_3)
        self.label_41.setGeometry(QtCore.QRect(20, 310, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_22.setGeometry(QtCore.QRect(110, 270, 61, 21))
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_32.setGeometry(QtCore.QRect(110, 310, 61, 21))
        self.lineEdit_32.setReadOnly(True)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(660, 50, 201, 141))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(670, 200, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(30, 30, 601, 321))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.toolBox.setFont(font)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 601, 213))
        self.page.setObjectName("page")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page)
        self.groupBox_2.setGeometry(QtCore.QRect(190, 0, 371, 211))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 61, 151))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(150, 70, 71, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(230, 70, 71, 51))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 51, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(150, 30, 60, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(210, 30, 51, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 110, 71, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 150, 71, 41))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(230, 130, 91, 61))
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 80, 51, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 150, 51, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_3.setGeometry(QtCore.QRect(80, 50, 61, 151))
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(270, 30, 31, 16))
        self.label_10.setObjectName("label_10")
        self.label_39 = QtWidgets.QLabel(self.groupBox_2)
        self.label_39.setGeometry(QtCore.QRect(90, 30, 31, 16))
        self.label_39.setObjectName("label_39")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(310, 30, 51, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.groupBox_4 = QtWidgets.QGroupBox(self.page)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 0, 181, 211))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox.setGeometry(QtCore.QRect(10, 50, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox.setFont(font)
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 90, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(10, 130, 61, 51))
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(100, 150, 71, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 601, 213))
        self.page_2.setObjectName("page_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 0, 261, 101))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_14.setGeometry(QtCore.QRect(150, 30, 81, 21))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_30 = QtWidgets.QLabel(self.groupBox_5)
        self.label_30.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.label_30.setObjectName("label_30")
        self.label_17 = QtWidgets.QLabel(self.groupBox_5)
        self.label_17.setGeometry(QtCore.QRect(20, 20, 71, 41))
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_27.setGeometry(QtCore.QRect(150, 70, 81, 21))
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.groupBox_7 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_7.setGeometry(QtCore.QRect(280, 0, 271, 101))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_13 = QtWidgets.QLabel(self.groupBox_7)
        self.label_13.setGeometry(QtCore.QRect(20, 40, 81, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_7)
        self.label_14.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_10.setGeometry(QtCore.QRect(160, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_11.setGeometry(QtCore.QRect(160, 70, 81, 21))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.groupBox_11 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_11.setGeometry(QtCore.QRect(0, 100, 261, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setObjectName("groupBox_11")
        self.label_31 = QtWidgets.QLabel(self.groupBox_11)
        self.label_31.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.groupBox_11)
        self.label_32.setGeometry(QtCore.QRect(20, 55, 111, 16))
        self.label_32.setObjectName("label_32")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_28.setGeometry(QtCore.QRect(150, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_28.setFont(font)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_29.setGeometry(QtCore.QRect(150, 55, 81, 21))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.label_33 = QtWidgets.QLabel(self.groupBox_11)
        self.label_33.setGeometry(QtCore.QRect(20, 80, 31, 16))
        self.label_33.setObjectName("label_33")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_30.setGeometry(QtCore.QRect(80, 80, 61, 21))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.label_34 = QtWidgets.QLabel(self.groupBox_11)
        self.label_34.setGeometry(QtCore.QRect(150, 80, 31, 16))
        self.label_34.setObjectName("label_34")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_31.setGeometry(QtCore.QRect(170, 80, 61, 21))
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.groupBox_10 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_10.setGeometry(QtCore.QRect(280, 100, 271, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setObjectName("groupBox_10")
        self.label_26 = QtWidgets.QLabel(self.groupBox_10)
        self.label_26.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_10)
        self.label_27.setGeometry(QtCore.QRect(20, 55, 111, 16))
        self.label_27.setObjectName("label_27")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_23.setGeometry(QtCore.QRect(160, 30, 81, 21))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setStyleSheet('background-color:gray')
        self.lineEdit_24 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_24.setGeometry(QtCore.QRect(160, 55, 81, 21))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setStyleSheet('background-color:gray')
        self.label_28 = QtWidgets.QLabel(self.groupBox_10)
        self.label_28.setGeometry(QtCore.QRect(20, 80, 31, 16))
        self.label_28.setObjectName("label_28")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_25.setGeometry(QtCore.QRect(90, 80, 61, 21))
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_25.setReadOnly(True)
        self.lineEdit_25.setStyleSheet('background-color:gray')
        self.lineEdit_26 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_26.setGeometry(QtCore.QRect(180, 80, 61, 21))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_26.setReadOnly(True)
        self.lineEdit_26.setStyleSheet('background-color:gray')
        self.label_29 = QtWidgets.QLabel(self.groupBox_10)
        self.label_29.setGeometry(QtCore.QRect(160, 80, 16, 16))
        self.label_29.setObjectName("label_29")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 601, 213))
        self.page_3.setObjectName("page_3")
        self.groupBox_8 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_8.setGeometry(QtCore.QRect(0, 0, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.label_15 = QtWidgets.QLabel(self.groupBox_8)
        self.label_15.setGeometry(QtCore.QRect(20, 40, 81, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_8)
        self.label_16.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.label_16.setObjectName("label_16")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_12.setGeometry(QtCore.QRect(120, 40, 91, 21))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_13.setGeometry(QtCore.QRect(120, 70, 91, 21))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.groupBox_6 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 100, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_11 = QtWidgets.QLabel(self.groupBox_6)
        self.label_11.setGeometry(QtCore.QRect(20, 30, 191, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_6)
        self.label_12.setGeometry(QtCore.QRect(20, 60, 41, 16))
        self.label_12.setObjectName("label_12")
        self.label_18 = QtWidgets.QLabel(self.groupBox_6)
        self.label_18.setGeometry(QtCore.QRect(130, 60, 21, 16))
        self.label_18.setObjectName("label_18")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_8.setGeometry(QtCore.QRect(60, 60, 61, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setStyleSheet('background-color:gray')
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_9.setGeometry(QtCore.QRect(150, 60, 61, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setStyleSheet('background-color:gray')
        self.groupBox_9 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_9.setGeometry(QtCore.QRect(260, 0, 211, 201))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setObjectName("groupBox_9")
        self.label_19 = QtWidgets.QLabel(self.groupBox_9)
        self.label_19.setGeometry(QtCore.QRect(20, 30, 41, 16))
        self.label_19.setObjectName("label_19")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_15.setGeometry(QtCore.QRect(60, 30, 71, 21))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_9)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 60, 71, 131))
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 60, 71, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 100, 71, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 140, 71, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.toolBox.addItem(self.page_3, "")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(30, 360, 601, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(60, 380, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(150, 380, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(250, 380, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.commandLinkButton_3.setFont(font)
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(350, 380, 111, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.commandLinkButton_4.setFont(font)
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(480, 380, 101, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.commandLinkButton_5.setFont(font)
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")
        self.groupBox_14 = QtWidgets.QGroupBox(Form)
        self.groupBox_14.setGeometry(QtCore.QRect(660, 260, 201, 141))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox_14.setFont(font)
        self.groupBox_14.setObjectName("groupBox_14")
        self.listWidget_4 = QtWidgets.QListWidget(self.groupBox_14)
        self.listWidget_4.setGeometry(QtCore.QRect(10, 30, 181, 101))
        self.listWidget_4.setWordWrap(True)
        self.listWidget_4.setObjectName("listWidget_4")
        self.listWidget_4.setStyleSheet('color:red')

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.num = 0
        self.error = 0
        self.error_list = []
        self.seed_list = []
        self.demand_list = []
        self.demand_prob_list = []
        self.csv_2 = 1
        self.exp_data = []
        self.rule_data = []
        self.tableWidget.setHorizontalHeaderLabels(['Sim time','Event'])
        self.tableWidget_2.setVerticalHeaderLabels(['Average ordering cost per month',
                                                  'Average holding cost per month',
                                                  'Average shortage cost per month',
                                                  'Average total cost per month',
                                                  'The number of items discarded',
                                                  'The proportion of items discarded',
                                                  'Expected proportion of backlog',
                                                  'Expected number of express orders'])
        self.tableWidget_3.setVerticalHeaderLabels(['Seed',
                                                    'Initial_inv_level',
                                                    'Mean interdemand',
                                                    'Number of demand',
                                                    'Demand list',
                                                    'Probability list',
                                                    'Evalution internal',
                                                    'Number of month',
                                                    'Holding cost',
                                                    'Shortage cost',
                                                    'Normal setup cost',
                                                    'Normal incremental cost',
                                                    'Express setup cost',
                                                    'Express incremental cost',
                                                    'Normal minlag',
                                                    'Normal maxlag',
                                                    'Express minlag',
                                                    'Express maxlag',
                                                    'Small s',
                                                    'Big s',
                                                    'Min overdue time',
                                                    'Max overdue time'
                                                    ])

        #设置监听器
        self.commandLinkButton.clicked.connect(self.run_1)
        self.commandLinkButton_2.clicked.connect(self.run_all)
        self.commandLinkButton_3.clicked.connect(self.reset)
        self.commandLinkButton_4.clicked.connect(self.table_clear)
        self.commandLinkButton_5.clicked.connect(self.save_data)
        self.checkBox.clicked.connect(self.is_checked_1)
        self.checkBox_2.clicked.connect(self.is_checked_2)
        self.pushButton_4.clicked.connect(self.add_2)
        self.pushButton_5.clicked.connect(self.delete_2)
        self.pushButton_6.clicked.connect(self.clear_2)
        self.pushButton.clicked.connect(self.add_1)
        self.pushButton_2.clicked.connect(self.delete_1)
        self.pushButton_3.clicked.connect(self.clear_1)
        self.buttonBox_2.accepted.connect(self.Show_pic)
        self.buttonBox_2.rejected.connect(self.Cancel_1)
        self.buttonBox.accepted.connect(self.Show_event)
        self.buttonBox.rejected.connect(self.Cancel_2)
        self.buttonBox_3.accepted.connect(self.Optimize)
        self.buttonBox_3.rejected.connect(self.Cancel_3)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Inventory Experiment"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Experiment data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Parameter"))
        self.groupBox.setTitle(_translate("Form", "Check the process of experiment"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("Form", "Figure"))
        self.groupBox_12.setTitle(_translate("Form", "Event list"))
        self.label_24.setText(_translate("Form", "Choose time section"))
        self.label_25.setText(_translate("Form", "from"))
        self.label_35.setText(_translate("Form", "to"))
        self.groupBox_13.setTitle(_translate("Form", "Figure"))
        self.label_36.setText(_translate("Form", "Choose time section"))
        self.label_37.setText(_translate("Form", "to"))
        self.label_38.setText(_translate("Form", "from"))
        self.groupBox_3.setTitle(_translate("Form", "Optimal (s,S)"))
        self.label_7.setText(_translate("Form", "Iterate small_s from"))
        self.label_20.setText(_translate("Form", "to"))
        self.label_9.setText(_translate("Form", "Iterate Big_s from"))
        self.label_21.setText(_translate("Form", "to"))
        self.label_22.setText(_translate("Form", "Run Time(s)"))
        self.label_40.setText(_translate("Form", "Optimal s"))
        self.label_41.setText(_translate("Form", "Optimal S"))
        self.label.setText(_translate("Form", " Inventory\n"
                                              "Experiment"))
        self.label_2.setText(_translate("Form", "WangHao,XuMingHai"))
        self.groupBox_2.setTitle(_translate("Form", "Demand Parameter"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "1"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "2"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "3"))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "4"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Form", "Add"))
        self.label_3.setText(_translate("Form", "Number of demand kinds"))
        self.label_4.setText(_translate("Form", "Demand"))
        self.label_5.setText(_translate("Form", "Demand"))
        self.pushButton_2.setText(_translate("Form", "Delete"))
        self.pushButton_3.setText(_translate("Form", "Clear"))
        self.label_6.setText(_translate("Form", "Mean interdemand per month"))
        self.lineEdit_2.setText(_translate("Form", "4"))
        self.lineEdit_3.setText(_translate("Form", "10"))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        item = self.listWidget_3.item(0)
        item.setText(_translate("Form", "0.163"))
        item = self.listWidget_3.item(1)
        item.setText(_translate("Form", "0.500"))
        item = self.listWidget_3.item(2)
        item.setText(_translate("Form", "0.833"))
        item = self.listWidget_3.item(3)
        item.setText(_translate("Form", "1.000"))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        self.label_10.setText(_translate("Form", "Prob"))
        self.label_39.setText(_translate("Form", "Prob"))
        self.groupBox_4.setTitle(_translate("Form", "Rule"))
        self.checkBox.setText(_translate("Form", "Express or not?"))
        self.checkBox_2.setText(_translate("Form", "Perishable or not?"))
        self.label_8.setText(_translate("Form", "Initial inventory level"))
        self.lineEdit_6.setText(_translate("Form", "10"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "Input 1"))
        self.groupBox_5.setTitle(_translate("Form", "Stimulation Time"))
        self.lineEdit_14.setText(_translate("Form", "1"))
        self.label_30.setText(_translate("Form", "Num of month"))
        self.label_17.setText(_translate("Form", "Evaluation Internal"))
        self.lineEdit_27.setText(_translate("Form", "120"))
        self.groupBox_7.setTitle(_translate("Form", "Cost Parameter"))
        self.label_13.setText(_translate("Form", "Holding cost"))
        self.label_14.setText(_translate("Form", "Shortage cost"))
        self.lineEdit_10.setText(_translate("Form", "1"))
        self.lineEdit_11.setText(_translate("Form", "5"))
        self.groupBox_11.setTitle(_translate("Form", "Normal Order"))
        self.label_31.setText(_translate("Form", "Setup cost"))
        self.label_32.setText(_translate("Form", "Incremental cost"))
        self.lineEdit_28.setText(_translate("Form", "32"))
        self.lineEdit_29.setText(_translate("Form", "3"))
        self.label_33.setText(_translate("Form", "Lag"))
        self.lineEdit_30.setText(_translate("Form", "0.5"))
        self.label_34.setText(_translate("Form", "to"))
        self.lineEdit_31.setText(_translate("Form", "1"))
        self.groupBox_10.setTitle(_translate("Form", "Express Order"))
        self.label_26.setText(_translate("Form", "Setup cost"))
        self.label_27.setText(_translate("Form", "Incremental cost"))
        self.label_28.setText(_translate("Form", "Lag"))
        self.label_29.setText(_translate("Form", "to"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "Input 2"))
        self.groupBox_8.setTitle(_translate("Form", "(s,S)"))
        self.label_15.setText(_translate("Form", "Small s"))
        self.label_16.setText(_translate("Form", "Big s"))
        self.lineEdit_12.setText(_translate("Form", "40"))
        self.lineEdit_13.setText(_translate("Form", "60"))
        self.groupBox_6.setTitle(_translate("Form", "Overdue Time"))
        self.label_11.setText(_translate("Form", "The overdue time for a item is"))
        self.label_12.setText(_translate("Form", "from"))
        self.label_18.setText(_translate("Form", "to"))
        self.groupBox_9.setTitle(_translate("Form", "Random Seed"))
        self.label_19.setText(_translate("Form", "Seed"))
        self.pushButton_4.setText(_translate("Form", "Add"))
        self.pushButton_5.setText(_translate("Form", "Delete"))
        self.pushButton_6.setText(_translate("Form", "Clear"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Form", "Input 3"))
        self.commandLinkButton.setText(_translate("Form", "Run"))
        self.commandLinkButton_2.setText(_translate("Form", "RunAll"))
        self.commandLinkButton_3.setText(_translate("Form", "Reset"))
        self.commandLinkButton_4.setText(_translate("Form", "Table Clear"))
        self.commandLinkButton_5.setText(_translate("Form", "Save Data"))
        self.groupBox_14.setTitle(_translate("Form", "Exception"))


    def Get_Parameter(self):
        import Inventory_Experiment as ie
        try:
            ie.initial_inv_level = int(self.lineEdit_6.text())
            ie.mean_interdemand = float(self.lineEdit_3.text())
            ie.number_of_demand = int(self.lineEdit_2.text())
            ie.evaluate_interval = float(self.lineEdit_14.text())
            ie.num_months = float(self.lineEdit_27.text())
            ie.holding_cost = float(self.lineEdit_10.text())
            ie.shortage_cost = float(self.lineEdit_11.text())
            ie.setup_cost = float(self.lineEdit_28.text())
            ie.incremental_cost = float(self.lineEdit_29.text())
            ie.minlag = float(self.lineEdit_30.text())
            ie.maxlag = float(self.lineEdit_31.text())
            ie.smalls = int(self.lineEdit_12.text())
            ie.bigs = int(self.lineEdit_13.text())
            if self.checkBox.isChecked():
                ie.choice_1 = '1'
                ie.setup_cost_2 = float(self.lineEdit_23.text())
                ie.incremental_cost_2 = float(self.lineEdit_24.text())
                ie.minlag_f = float(self.lineEdit_25.text())
                ie.maxlag_f = float(self.lineEdit_26.text())
            else:
                ie.choice_1 = '0'
            if self.checkBox_2.isChecked():
                ie.choice_2 = '1'
                ie.overdue_min = float(self.lineEdit_8.text())
                ie.overdue_max = float(self.lineEdit_9.text())
            else:
                ie.choice_2 = '0'
        except(ValueError):
            self.Exception("The input line can't be NULL or Alphabet!")

    def is_checked_1(self):
        if self.checkBox.isChecked():
            self.lineEdit_23.setText('48')
            self.lineEdit_23.setReadOnly(False)
            self.lineEdit_23.setStyleSheet('background-color:white')
            self.lineEdit_24.setText('4')
            self.lineEdit_24.setReadOnly(False)
            self.lineEdit_24.setStyleSheet('background-color:white')
            self.lineEdit_25.setText('0.25')
            self.lineEdit_25.setReadOnly(False)
            self.lineEdit_25.setStyleSheet('background-color:white')
            self.lineEdit_26.setText('0.5')
            self.lineEdit_26.setReadOnly(False)
            self.lineEdit_26.setStyleSheet('background-color:white')
        else:
            self.lineEdit_23.clear()
            self.lineEdit_23.setReadOnly(True)
            self.lineEdit_23.setStyleSheet('background-color:gray')
            self.lineEdit_24.clear()
            self.lineEdit_24.setReadOnly(True)
            self.lineEdit_24.setStyleSheet('background-color:gray')
            self.lineEdit_25.clear()
            self.lineEdit_25.setReadOnly(True)
            self.lineEdit_25.setStyleSheet('background-color:gray')
            self.lineEdit_26.clear()
            self.lineEdit_26.setReadOnly(True)
            self.lineEdit_26.setStyleSheet('background-color:gray')

    def is_checked_2(self):
        if self.checkBox_2.isChecked():
            self.lineEdit_8.setText('1.5')
            self.lineEdit_8.setReadOnly(False)
            self.lineEdit_8.setStyleSheet('background-color:white')
            self.lineEdit_9.setText('2.5')
            self.lineEdit_9.setReadOnly(False)
            self.lineEdit_9.setStyleSheet('background-color:white')
        else:
            self.lineEdit_8.clear()
            self.lineEdit_8.setReadOnly(True)
            self.lineEdit_8.setStyleSheet('background-color:gray')
            self.lineEdit_9.clear()
            self.lineEdit_9.setReadOnly(True)
            self.lineEdit_9.setStyleSheet('background-color:gray')

    def Iter_seed(self):
        seed_list = []
        for i in range(self.listWidget_2.count()):
            try:
                seed_list.append(self.listWidget_2.item(i).text())
            except(AttributeError):
                if i == 0:
                    seed_list = [-1]
                break
        return seed_list

    def Show_result(self,i):
        import Inventory_Experiment as ie
        result = ie.result_list
        self.tableWidget_2.setColumnCount(self.num+1)
        for j in range(len(result)):
            item = QtWidgets.QTableWidgetItem(result[j])
            self.tableWidget_2.setItem(j,int(i),item)

    def Show_parameter(self,i):
        import Inventory_Experiment as ie
        parameter_list = [str(ie.seed),self.lineEdit_6.text(),self.lineEdit_3.text(),self.lineEdit_2.text(),
                          ''.join(ie.distrib_demand.__str__()),''.join(ie.prob_distrib_demand.__str__()),
                          self.lineEdit_14.text(),self.lineEdit_27.text(),self.lineEdit_10.text(),
                          self.lineEdit_11.text(),self.lineEdit_28.text(),self.lineEdit_29.text(),
                          self.lineEdit_23.text(),self.lineEdit_24.text(),self.lineEdit_30.text(),
                          self.lineEdit_31.text(),self.lineEdit_25.text(),self.lineEdit_26.text(),
                          self.lineEdit_12.text(),self.lineEdit_13.text(),self.lineEdit_8.text(),self.lineEdit_9.text()]
        self.tableWidget_3.setColumnCount(self.num+1)
        for j in range(len(parameter_list)):
            item = QtWidgets.QTableWidgetItem(parameter_list[j])
            self.tableWidget_3.setItem(j,int(i),item)
        self.num += 1

    def Get_rand(self):
        import Inventory_Experiment as ie
        rand_list = []
        demand_list = []
        self.lineEdit_2.setText(str(self.listWidget.count()))
        try:
            for i in range(self.listWidget.count()):
                demand_list.append(int(self.listWidget.item(i).text()))
                rand_list.append(float(self.listWidget_3.item(i).text()))
        except(AttributeError):
            self.Exception("The length of demand list is not equal to that of prob list!")
        ie.prob_distrib_demand = rand_list
        ie.distrib_demand = demand_list

    def run_1(self):
        import Inventory_Experiment as ie
        self.error = 0
        self.Get_rand()
        self.Get_Parameter()
        if self.error == 0:
            self.listWidget_4.clear()
            seed = self.listWidget_2.currentRow()
            ie.seed = int(seed)
            try:
                ie.Run()
            except(TypeError):
                self.Exception("The maximum probability of demands must be 1!")
            else:
                self.Show_result(self.num)
                self.Show_parameter(self.num)
                self.label_23.setPixmap(QPixmap('Pic_data/Inventory/Inventory.png'))

    def run_all(self):
        import Inventory_Experiment as ie
        self.error = 0
        self.Get_rand()
        seed_list = self.Iter_seed()
        self.Get_Parameter()
        if self.error == 0:
            try:
                for i in range(len(seed_list)):
                    ie.seed = int(seed_list[i])
                    ie.Run()
                    self.Show_result(self.num)
                    self.Show_parameter(self.num)
                self.label_23.setPixmap(QPixmap('Pic_data/Inventory/Inventory.png'))
            except:
                self.Exception("The maximum probability of demands must be 1!")
            else:
                self.listWidget_4.clear()

    def add_1(self):
        self.demand_prob_list = []
        self.demand_list = []
        if self.lineEdit_7.text() != '':
            self.demand_prob_list.append(self.lineEdit_7.text())
            self.listWidget_3.addItems(self.demand_prob_list)
        self.lineEdit_7.clear()
        if self.lineEdit.text() != '':
            self.demand_list.append(self.lineEdit.text())
            self.listWidget.addItems(self.demand_list)
        self.lineEdit.clear()

    def delete_1(self):
        if self.listWidget.currentRow() != -1:
            self.listWidget.takeItem(self.listWidget.currentRow())
            self.listWidget_3.setCurrentRow(-1)
        self.listWidget_3.takeItem(self.listWidget_3.currentRow())
        self.listWidget.setCurrentRow(-1)

    def clear_1(self):
        self.listWidget.clear()
        self.listWidget_3.clear()
        self.lineEdit.clear()
        self.lineEdit_7.clear()

    def add_2(self):
        self.seed_list = []
        self.seed_list.append(self.lineEdit_15.text())
        self.listWidget_2.addItems(self.seed_list)
        self.lineEdit_15.clear()

    def delete_2(self):
        self.listWidget_2.takeItem(self.listWidget_2.currentRow())

    def clear_2(self):
        self.listWidget_2.clear()
        self.lineEdit_15.clear()

    def reset(self):
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.lineEdit_6.setText('10')
        self.listWidget.addItems(['1','2','3','4'])
        self.listWidget_3.addItems(['0.163','0.500','0.833','1.000'])
        self.lineEdit.clear()
        self.lineEdit_7.clear()
        self.lineEdit_2.setText('4')
        self.lineEdit_3.setText('10')
        self.lineEdit_14.setText('1')
        self.lineEdit_27.setText('120')
        self.lineEdit_10.setText('1')
        self.lineEdit_11.setText('5')
        self.lineEdit_28.setText('32')
        self.lineEdit_29.setText('3')
        self.lineEdit_30.setText('0.5')
        self.lineEdit_31.setText('1')
        self.lineEdit_23.setText('48')
        self.lineEdit_24.setText('4')
        self.lineEdit_25.setText('0.25')
        self.lineEdit_26.setText('0.5')
        self.lineEdit_12.setText('40')
        self.lineEdit_13.setText('60')
        self.lineEdit_8.setText('1.5')
        self.lineEdit_9.setText('2.5')
        self.lineEdit_15.clear()
        self.listWidget_2.clear()

    def table_clear(self):
        self.tableWidget_2.clearContents()
        self.tableWidget_3.clearContents()
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_3.setColumnCount(0)
        self.num = 0

    def save_data(self):
        columns = self.tableWidget_2.columnCount()
        rows = self.tableWidget_2.rowCount()
        for i in range(columns):
            data = []
            for j in range(rows):
                data.append(self.tableWidget_2.item(j, i).text())
            data.append(' ')
            self.exp_data.append(data)
        columns = self.tableWidget_3.columnCount()
        rows = self.tableWidget_3.rowCount()
        for i in range(columns):
            data = []
            for j in range(rows):
                data.append(self.tableWidget_3.item(j, i).text())
            self.rule_data.append(data)
        csv_1 = pd.DataFrame(self.exp_data, columns=['Average ordering cost per month',
                                                  'Average holding cost per month',
                                                  'Average shortage cost per month',
                                                  'Average total cost per month',
                                                  'The number of items discarded',
                                                  'The proportion of items discarded',
                                                  'Expected proportion of backlog',
                                                  'Expected number of express orders',''])
        csv_2 = pd.DataFrame(self.rule_data, columns=['Seed',
                                                    'Initial_inv_level',
                                                    'Mean interdemand',
                                                    'Number of demand',
                                                    'Demand list',
                                                    'Probability list',
                                                    'Evalution internal',
                                                    'Number of month',
                                                    'Holding cost',
                                                    'Shortage cost',
                                                    'Normal setup cost',
                                                    'Normal incremental cost',
                                                    'Express setup cost',
                                                    'Express incremental cost',
                                                    'Normal minlag',
                                                    'Normal maxlag',
                                                    'Express minlag',
                                                    'Express maxlag',
                                                    'Small s',
                                                    'Big s',
                                                    'Min overdue time',
                                                    'Max overdue time'
                                                    ])
        csv = pd.DataFrame.join(csv_1, csv_2).T
        csv.to_csv('./File_data/Inventory/Inventory_Experiment_' + str(self.csv_2) + '.csv')
        self.csv_2 += 1

    def Show_pic(self):
        import Inventory_Experiment as ie
        try:
            p = int(self.lineEdit_20.text())
            q = int(self.lineEdit_21.text())
        except:
            self.Exception("The input line can't be NULL or Alphabet!")
        else:
            try:
                self.listWidget_4.clear()
                ie.Plot_inv(p,q)
                self.label_23.setPixmap(QPixmap('Pic_data/Inventory/Inventory.png'))
            except(UnboundLocalError):
                self.Exception("The time section you choose is out of bound!")

    def Cancel_1(self):
        self.label_23.clear()
        self.lineEdit_20.clear()
        self.lineEdit_21.clear()

    def Cache_clear(self):
        file = os.walk('File_data/Inventory')
        for i in file.__next__()[2]:
            os.remove('File_data/Inventory/'+i)

    def Show_event(self):
        try:
            a = int(self.lineEdit_18.text())
            b = int(self.lineEdit_19.text())
        except:
            self.Exception("The input line can't be NULL or Alphabet!")
        else:
            try:
                self.listWidget_4.clear()
                event = pd.read_csv('Inventory_data/event.csv')
                event = event.values[:,1:]
                for i in range(len(event[:,0])):
                    if a <= event[i,0]:
                        m = i
                        break
                for i in range(len(event[:,0])):
                    if b <= event[i,0]:
                        n = i-1
                        break
                self.tableWidget.setColumnCount(len(event[0,:]))
                self.tableWidget.setRowCount(len(event[m:n,0]))
                self.tableWidget.setHorizontalHeaderLabels(['Sim time','Event'])
                self.tableWidget.setColumnWidth(0,90)
                self.tableWidget.setColumnWidth(1,400)
                for j in range(len(event[0, :])):
                    for i in range(n-m):
                        item = QtWidgets.QTableWidgetItem(str(event[m+i,j]))
                        self.tableWidget.setItem(i,j,item)
            except(UnboundLocalError):
                self.Exception("The time section you choose is out of bound!")

    def Cancel_2(self):
        self.tableWidget.clearContents()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.lineEdit_18.clear()
        self.lineEdit_19.clear()

    def Optimize(self):
        import Inventory_Experiment as ie
        try:
            ie.min_s = int(self.lineEdit_4.text())
            ie.max_s = int(self.lineEdit_5.text())
            ie.min_S = int(self.lineEdit_17.text())
            ie.max_S = int(self.lineEdit_16.text())
        except:
            self.Exception("The input line can't be NULL or Alphabet!")
        else:
            if int(self.lineEdit_17.text())<=int(self.lineEdit_5.text()):
                self.Exception("The min big_s must be greater than the max small_s!")
            else:
                self.listWidget_4.clear()
                start = time.time()
                s,S,cost_list = ie.Opimizer()
                end = time.time()
                self.lcdNumber.display(end-start)
                self.lineEdit_22.setText(str(s))
                self.lineEdit_32.setText(str(S))
                ie.Plot_surf(cost_list)

    def Cancel_3(self):
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_17.clear()
        self.lineEdit_16.clear()
        self.lineEdit_22.clear()
        self.lineEdit_32.clear()
        self.lcdNumber.display(0)

    def Exception(self,error):
        self.error_list = []
        self.error_list.append(error)
        self.listWidget_4.addItems(self.error_list)
        self.error = 1


'''主函数'''
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_Form()
    #MainWindow.showFullScreen()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())

