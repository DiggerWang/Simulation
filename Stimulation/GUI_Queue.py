# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Queue.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
#import Queuing_Experiment
import sys
import os
import pandas as pd

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1440, 900)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(450, 100, 461, 281))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 50, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(200, 50, 101, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 100, 101, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 150, 101, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 170, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setToolTipDuration(0)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 50, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setToolTipDuration(0)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(70, 0, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab)
        self.pushButton_13.setGeometry(QtCore.QRect(340, 110, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setToolTipDuration(0)
        self.pushButton_13.setAutoFillBackground(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 100, 101, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 100, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 50, 101, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 150, 101, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(30, 150, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(30, 50, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 170, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setToolTipDuration(0)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(340, 50, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setToolTipDuration(0)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(130, 0, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_14.setGeometry(QtCore.QRect(340, 110, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setToolTipDuration(0)
        self.pushButton_14.setAutoFillBackground(False)
        self.pushButton_14.setObjectName("pushButton_14")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(200, 100, 101, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(30, 100, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(200, 50, 101, 25))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(200, 150, 101, 25))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(30, 150, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(30, 50, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(30, 200, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(200, 200, 101, 25))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(340, 50, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setToolTipDuration(0)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 170, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setToolTipDuration(0)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(130, 0, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_15.setGeometry(QtCore.QRect(340, 110, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setToolTipDuration(0)
        self.pushButton_15.setAutoFillBackground(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.tabWidget.addTab(self.tab_3, "")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(80, 90, 291, 261))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_11.setGeometry(QtCore.QRect(180, 44, 71, 25))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(130, 50, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(160, 90, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setToolTipDuration(0)
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(160, 150, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setToolTipDuration(0)
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setGeometry(QtCore.QRect(160, 210, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setToolTipDuration(0)
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(20, 30, 91, 221))
        self.listWidget.setObjectName("listWidget")
        self.tabWidget_2 = QtWidgets.QTabWidget(Form)
        self.tabWidget_2.setGeometry(QtCore.QRect(830, 440, 551, 411))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(0, -10, 541, 391))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("Queue_1.png"))
        self.label_15.setObjectName("label_15")
        self.label_15.setScaledContents(True)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(980, 100, 361, 251))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(40, 60, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(40, 110, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(190, 110, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(90, 110, 81, 25))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(220, 110, 81, 25))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_10.setGeometry(QtCore.QRect(90, 170, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setToolTipDuration(0)
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_11.setGeometry(QtCore.QRect(200, 170, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setToolTipDuration(0)
        self.pushButton_11.setAutoFillBackground(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(560, 10, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(33)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(1230, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setUnderline(False)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(110, 370, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.setAutoFillBackground(True)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.tabWidget_3 = QtWidgets.QTabWidget(Form)
        self.tabWidget_3.setGeometry(QtCore.QRect(60, 440, 701, 411))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tabWidget_3.setFont(font)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_5)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 701, 381))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 699, 379))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 701, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(13)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_6)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 0, 701, 381))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 699, 379))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 701, 381))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(6)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget_3.addTab(self.tab_6, "")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(260, 370, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.commandLinkButton_3.setFont(font)
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setAutoFillBackground(True)
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(1040, 370, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_2.setAutoFillBackground(True)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.num = 0
        self.csv = 1
        self.csv_2 = 1
        self.exp_data = []
        self.rule_data = []

        #初始textline值
        self.lineEdit.setText('1')
        self.lineEdit_2.setText('0.5')
        self.lineEdit_3.setText('400')
        self.lineEdit_5.setText('1')
        self.lineEdit_4.setText('0.5')
        self.lineEdit_6.setText('480')
        self.lineEdit_8.setText('1')
        self.lineEdit_7.setText('0.5')
        self.lineEdit_9.setText('480')
        self.lineEdit_10.setText('100')

        self.tableWidget.setVerticalHeaderLabels(['The average delay in queue',
                                                  'The average length of the queue',
                                                  'Utilization',
                                                  'The time-average number in the system',
                                                  'The average total time in the system',
                                                  'The maximum queue length',
                                                  'The maximum delay in queue',
                                                  'The maximum time in the system',
                                                  'Customers queueing over 1 minute',
                                                  'The number of customers balked',
                                                  'The number of customers served',
                                                  'The number of customers delayed',
                                                  'The simulation time'])

        #设置监听器
        self.pushButton_2.clicked.connect(self.on_click_Run_1)
        self.pushButton_4.clicked.connect(self.on_click_Reset_1)
        self.pushButton_6.clicked.connect(self.on_click_Run_2)
        self.pushButton_5.clicked.connect(self.on_click_Reset_2)
        self.pushButton.clicked.connect(self.on_click_Run_3)
        self.pushButton_3.clicked.connect(self.on_click_Reset_3)
        self.pushButton_7.clicked.connect(self.on_click_Add)
        self.pushButton_8.clicked.connect(self.on_click_Delete)
        self.pushButton_9.clicked.connect(self.on_click_Clear)
        self.pushButton_13.clicked.connect(self.on_click_RunAll_1)
        self.pushButton_14.clicked.connect(self.on_click_RunAll_2)
        self.pushButton_15.clicked.connect(self.on_click_RunAll_3)
        self.commandLinkButton.clicked.connect(self.on_click_Tablereset)
        self.pushButton_10.clicked.connect(self.on_click_Run_4)
        self.pushButton_11.clicked.connect(self.on_click_Reset_4)
        self.commandLinkButton_2.clicked.connect(self.pic_reset)
        self.commandLinkButton_3.clicked.connect(self.save_data)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Queueing Experiment"))
        self.label.setText(_translate("Form", "Mean arrival time"))
        self.label_2.setText(_translate("Form", "Mean service time"))
        self.label_3.setText(_translate("Form", "Number of customs"))
        self.pushButton_4.setText(_translate("Form", "Reset"))
        self.pushButton_2.setText(_translate("Form", "Run"))
        self.label_11.setText(_translate("Form", "Rule1: Fixed number of serviced custiomers rule"))
        self.pushButton_13.setText(_translate("Form", "RunAll"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Rule1"))
        self.label_4.setText(_translate("Form", "Mean service time"))
        self.label_5.setText(_translate("Form", "Total simulation time"))
        self.label_6.setText(_translate("Form", "Mean arrival time"))
        self.pushButton_5.setText(_translate("Form", "Reset"))
        self.pushButton_6.setText(_translate("Form", "Run"))
        self.label_12.setText(_translate("Form", "Rule2: Fixed service time rule"))
        self.pushButton_14.setText(_translate("Form", "RunAll"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Rule2"))
        self.label_7.setText(_translate("Form", "Mean service time"))
        self.label_8.setText(_translate("Form", "Total simulation time"))
        self.label_9.setText(_translate("Form", "Mean arrival time"))
        self.label_10.setText(_translate("Form", "Max length of queue"))
        self.pushButton.setText(_translate("Form", "Run"))
        self.pushButton_3.setText(_translate("Form", "Reset"))
        self.label_13.setText(_translate("Form", "Rule3: Fixed queue length rule"))
        self.pushButton_15.setText(_translate("Form", "RunAll"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Rule3"))
        self.groupBox.setTitle(_translate("Form", "Seed List"))
        self.label_14.setText(_translate("Form", "Seed"))
        self.pushButton_7.setText(_translate("Form", "Add"))
        self.pushButton_8.setText(_translate("Form", "Delete"))
        self.pushButton_9.setText(_translate("Form", "Clear"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Form", "Figure"))
        self.groupBox_2.setTitle(_translate("Form", "Additional choice"))
        self.label_16.setText(_translate("Form", "Choose time section:"))
        self.label_17.setText(_translate("Form", "From"))
        self.label_18.setText(_translate("Form", "to"))
        self.pushButton_10.setText(_translate("Form", "Run"))
        self.pushButton_11.setText(_translate("Form", "Reset"))
        self.label_20.setText(_translate("Form", "Queueing Experiment"))
        self.label_21.setText(_translate("Form", "XuMingHai,WangHao"))
        self.commandLinkButton.setText(_translate("Form", "Tabel Reset"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("Form", "Experiment Result"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("Form", "Rule Data"))
        self.commandLinkButton_3.setText(_translate("Form", "Data Save"))
        self.commandLinkButton_2.setText(_translate("Form", "Pic Reset"))


    def Get_Parameter_1(self):
        return float(self.lineEdit.text()),1/float(self.lineEdit_2.text()),float(self.lineEdit_3.text()),1.0e+30

    def Get_Parameter_2(self):
        return float(self.lineEdit_5.text()),1/float(self.lineEdit_4.text()),float(self.lineEdit_6.text()),1.0e+30

    def Get_Parameter_3(self):
        return float(self.lineEdit_8.text()),1/float(self.lineEdit_7.text()),float(self.lineEdit_9.text()),float(self.lineEdit_10.text())

    def Show_result(self,i):
        import Queuing_Experiment
        result = Queuing_Experiment.result_list
        self.tableWidget.setColumnCount(self.num+1)
        for j in range(len(result)):
            item = QtWidgets.QTableWidgetItem(result[j])
            self.tableWidget.setItem(j,int(i),item)
        #self.num += 1


    def Show_data(self,i):
        import Queuing_Experiment
        if Queuing_Experiment.rule == 1:
            data = ['Rule1: Fixed number of serviced custiomers rule',
                    'Seed: '+str(Queuing_Experiment.seed),
                    'Mean arrival time: '+self.lineEdit.text(),
                    'Mean service time: '+self.lineEdit_2.text(),
                    'Number of customs: '+self.lineEdit_3.text()]
        elif Queuing_Experiment.rule == 2:
            data = ['Rule2: Fixed service time rule',
                    'Seed: '+str(Queuing_Experiment.seed),
                    'Mean arrival time: '+self.lineEdit_5.text(),
                    'Mean service time:'+self.lineEdit_4.text(),
                    'Total simulation time:'+self.lineEdit_6.text()]
        elif Queuing_Experiment.rule == 3:
            data = ['Rule3: Fixed queue length rule',
                    'Seed: '+str(Queuing_Experiment.seed),
                    'Mean arrival time:'+self.lineEdit_8.text(),
                    'Mean service time: '+self.lineEdit_7.text(),
                    'Total simulation time: '+self.lineEdit_9.text(),
                    'Max length of queue: '+self.lineEdit_10.text()]
        self.tableWidget_2.setColumnCount(self.num+1)
        for j in range(len(data)):
            item_1 = QtWidgets.QTableWidgetItem(data[j])
            self.tableWidget_2.setColumnWidth(int(i), 200)
            self.tableWidget_2.setItem(j,int(i),item_1)
        self.num += 1


    def Iter_seed(self):
        seed_list = []
        for i in range(self.listWidget.count()):
            try:
                seed_list.append(self.listWidget.item(i).text())
            except(AttributeError):
                if i == 0:
                    seed_list = [-1]
                break
        return seed_list

    def on_click_Run_1(self):
        import Queuing_Experiment
        Queuing_Experiment.rule = 1
        Queuing_Experiment.mean_interarrival,Queuing_Experiment.mean_service,Queuing_Experiment.cus_num,Queuing_Experiment.Queue_limit = self.Get_Parameter_1()
        seed = self.listWidget.currentRow()
        Queuing_Experiment.seed = int(seed)
        Queuing_Experiment.Run()
        self.Show_result(self.num)
        self.Show_data(self.num)
        self.label_15.setPixmap(QPixmap("./Pic_data/Queue/Queue_1.png"))

    def on_click_Reset_1(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()

    def on_click_Run_2(self):
        import Queuing_Experiment
        Queuing_Experiment.rule = 2
        Queuing_Experiment.mean_interarrival, Queuing_Experiment.mean_service, Queuing_Experiment.time_end, Queuing_Experiment.Queue_limit = self.Get_Parameter_2()
        seed = self.listWidget.currentRow()
        Queuing_Experiment.seed = int(seed)
        Queuing_Experiment.Run()
        self.Show_result(self.num)
        self.Show_data(self.num)
        self.label_15.setPixmap(QPixmap("./Pic_data/Queue/Queue_1.png"))

    def on_click_Reset_2(self):
        self.lineEdit_5.clear()
        self.lineEdit_4.clear()
        self.lineEdit_6.clear()

    def on_click_Run_3(self):
        import Queuing_Experiment
        Queuing_Experiment.rule = 3
        Queuing_Experiment.mean_interarrival, Queuing_Experiment.mean_service, Queuing_Experiment.time_end, Queuing_Experiment.Queue_limit = self.Get_Parameter_3()
        seed = self.listWidget.currentRow()
        Queuing_Experiment.seed = int(seed)
        Queuing_Experiment.Run()
        self.Show_result(self.num)
        self.Show_data(self.num)
        self.label_15.setPixmap(QPixmap("./Pic_data/Queue/Queue_1.png"))

    def on_click_Reset_3(self):
        self.lineEdit_8.clear()
        self.lineEdit_7.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()

    def on_click_Add(self):
        self.seed_list = []
        self.seed_list.append(self.lineEdit_11.text())
        self.listWidget.addItems(self.seed_list)
        self.lineEdit_11.clear()

    def on_click_Delete(self):
        self.listWidget.takeItem(self.listWidget.currentRow())

    def on_click_Clear(self):
        self.listWidget.clear()
        self.lineEdit_11.clear()

    def on_click_RunAll_1(self):
        import Queuing_Experiment
        Queuing_Experiment.rule = 1
        Queuing_Experiment.mean_interarrival,Queuing_Experiment.mean_service,Queuing_Experiment.cus_num,Queuing_Experiment.Queue_limit = self.Get_Parameter_1()
        seed_list = self.Iter_seed()
        for i in range(len(seed_list)):
            Queuing_Experiment.seed = int(seed_list[i])
            Queuing_Experiment.Run()
            self.Show_result(self.num)
            self.Show_data(self.num)
        self.label_15.setPixmap(QPixmap("./Pic_data/Queue/Queue_1.png"))

    def on_click_RunAll_2(self):
        import Queuing_Experiment
        Queuing_Experiment.rule = 2
        Queuing_Experiment.mean_interarrival, Queuing_Experiment.mean_service, Queuing_Experiment.time_end, Queuing_Experiment.Queue_limit = self.Get_Parameter_2()
        seed_list = self.Iter_seed()
        for i in range(len(seed_list)):
            Queuing_Experiment.seed = int(seed_list[i])
            Queuing_Experiment.Run()
            self.Show_result(self.num)
            self.Show_data(self.num)
        self.label_15.setPixmap(QPixmap("./Pic_data/Queue/Queue_1.png"))

    def on_click_RunAll_3(self):
        import Queuing_Experiment
        Queuing_Experiment.rule = 3
        Queuing_Experiment.mean_interarrival, Queuing_Experiment.mean_service, Queuing_Experiment.time_end, Queuing_Experiment.Queue_limit = self.Get_Parameter_3()
        seed_list = self.Iter_seed()
        for i in range(len(seed_list)):
            Queuing_Experiment.seed = int(seed_list[i])
            Queuing_Experiment.Run()
            self.Show_result(self.num)
            self.Show_data(self.num)
        self.label_15.setPixmap(QPixmap("./Pic_data/Queue/Queue_1.png"))

    def on_click_Tablereset(self):
        self.num = 0
        self.tableWidget.clearContents()
        self.tableWidget_2.clearContents()
        self.tableWidget.setColumnCount(0)
        self.tableWidget_2.setColumnCount(0)

    def on_click_Run_4(self):
        import Queuing_Experiment
        i = int(self.lineEdit_12.text())
        j = int(self.lineEdit_13.text())
        Queuing_Experiment.Plot_2(i,j)
        self.label_15.setPixmap(QPixmap("./Pic_data/Queue/Queue_"+str(i)+"_"+str(j)+".png"))
        os.remove("./Pic_data/Queue/Queue_"+str(i)+"_"+str(j)+".png")

    def on_click_Reset_4(self):
        self.lineEdit_12.clear()
        self.lineEdit_13.clear()

    def on_click_Read(self):
        import Queuing_Experiment
        Queuing_Experiment.Write(self.csv)
        self.csv += 1

    def save_data(self):
        columns = self.tableWidget.columnCount()
        rows = self.tableWidget.rowCount()
        for i in range(columns):
            data = []
            for j in range(rows):
                data.append(self.tableWidget.item(j,i).text())
            self.exp_data.append(data)
        columns = self.tableWidget_2.columnCount()
        rows = self.tableWidget_2.rowCount()
        for i in range(columns):
            data = []
            for j in range(rows):
                data.append(self.tableWidget_2.item(j,i).text())
            self.rule_data.append(data)
        csv_1 = pd.DataFrame(self.exp_data,columns=('The average delay in queue',
                                                  'The average length of the queue',
                                                  'Utilization',
                                                  'The time-average number in the system',
                                                  'The average total time in the system',
                                                  'The maximum queue length',
                                                  'The maximum delay in queue',
                                                  'The maximum time in the system',
                                                  'Customers queueing over 1 minute',
                                                  'The number of customers balked',
                                                  'The number of customers served',
                                                  'The number of customers delayed',
                                                  'The simulation time'))
        csv_2 = pd.DataFrame(self.rule_data)
        csv = pd.DataFrame.join(csv_1,csv_2)
        csv.to_csv('./File_data/Queue/Queueing_Experiment_'+str(self.csv_2)+'.csv')
        self.csv_2 += 1

    def pic_reset(self):
        self.label_15.clear()


'''主函数'''
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_Form()
    #MainWindow.showFullScreen()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())





