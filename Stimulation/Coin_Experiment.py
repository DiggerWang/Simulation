# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Coin_Experiment.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import (QtCore, QtGui, QtWidgets)
import sys
import random
import pandas as pd
from PyQt5.QtGui import QIcon, QPixmap
from matplotlib import pyplot as plt

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(896, 650)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 20, 451, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 90, 611, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 400, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(220, 190, 91, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 240, 91, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 290, 91, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 350, 91, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 400, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAcceptDrops(False)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 170, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 240, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 290, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(70, 340, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(70, 470, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_5.setGeometry(QtCore.QRect(220, 470, 91, 21))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(220, 520, 91, 21))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setClearButtonEnabled(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(70, 520, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(350, 220, 491, 311))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 481, 281))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_9.setScaledContents(True)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 481, 281))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_10.setScaledContents(True)
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)


        # 设置按钮监听器
        self.pushButton.clicked.connect(self.on_click_OK)
        self.pushButton_2.clicked.connect(self.on_click_Reset)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Coin Experiment"))
        self.label.setText(_translate("Form", "Experiment Introduction"))
        self.label_2.setText(_translate("Form", "Participators spend certain cost(C) to throw a coin. When the difference between heads and tails equals to D，they can get the reward(R)."))
        self.pushButton.setText(_translate("Form", "Run"))
        self.pushButton_2.setText(_translate("Form", "Reset"))
        self.label_3.setText(_translate("Form", "The difference between heads and tails(D)"))
        self.label_4.setText(_translate("Form", "Cost per throw(C)"))
        self.label_5.setText(_translate("Form", "The promissory reward(R)"))
        self.label_6.setText(_translate("Form", "Stimulation times"))
        self.label_7.setText(_translate("Form", "Expected Cost"))
        self.label_8.setText(_translate("Form", "Expected Return"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Figure 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Figure 2"))

    # 定义实验的函数
    def Experiment(self):
        head = 0
        tail = 0
        cost = 0
        num = 0 #每一次实验最终抛的次数
        list_cost = []
        list_head = []
        list_tail = []
        list_num = []
        for i in range(0, int(self.lineEdit_4.text())):

            while (abs(head - tail) != int(self.lineEdit.text())):
                num += 1
                if(random.choice([0,1]) == 0):
                    head += 1
                else:
                    tail += 1
                cost += int(self.lineEdit_2.text())

            list_cost.append(cost)
            list_head.append(head)
            list_tail.append(tail)
            list_num.append(num)
            head = 0
            tail = 0
            cost = 0
            num = 0
            
        Total_cost = 0.0
        for i in list_cost:
            Total_cost += i

        Exp_cost = round(Total_cost / int(self.lineEdit_4.text()),3)
        Exp_return = round(int(self.lineEdit_3.text()) - Exp_cost,3)

        self.lineEdit_5.setText(str(Exp_cost))
        self.lineEdit_6.setText(str(Exp_return))

        return list_cost,list_head,list_tail,list_num,Exp_cost,Exp_return

    # 定义清空函数
    def Clear(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.label_9.clear()
        self.label_10.clear()

    def on_click_OK(self):
        self.Experiment()
        self.Plot()

    def on_click_Reset(self):
        self.Clear()

    #画图
    def Plot(self):
        list_cost,list_head,list_tail,list_num,Exp_cost,Exp_return = self.Experiment()
        x = range(1,int(self.lineEdit_4.text())+1)
        y1 = list_num
        y2 = list_head
        y3 = list_tail
        y4 = list_cost
        y5 = Exp_cost
        y6 = Exp_return
        y7=pd.Series(y4)
        y7=y7.cumsum()/x
        
        plt.plot(x,y1,color = '#00BFFF', linewidth=0.7,label = "The number of Throw-Times")
        #plt.plot(x, y2, color = 'red',linewidth=0.01,label = "The number of Head")
        #plt.plot(x, y3, color = 'blue',linewidth=0.01,label = "The number of Tail")
        plt.legend(loc="best")
        plt.savefig("./Pic_data/Coin/1.png",bbox_inches = "tight")
        self.label_9.setPixmap(QPixmap("./Pic_data/Coin/1.png"))

        plt.figure()
        plt.plot(x, y7, color = "coral", linewidth=0.7,label = "Cumulative Average Cost")
        #plt.axhline(y5, color = "red", linewidth = 4, label = "The Expected Cost")
        #plt.axhline(y6, color = "blue", linewidth = 4, label = "The Expected Return")
        plt.legend(loc="best")
        plt.savefig("./Pic_data/Coin/2.png",bbox_inches = "tight")
        self.label_10.setPixmap(QPixmap("./Pic_data/Coin/2.png"))
        plt.figure()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


