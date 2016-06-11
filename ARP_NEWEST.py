# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ArpCap.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import time
import arp_backend 
from PyQt4 import QtCore, QtGui
import customUI_rc
from PyQt4.Qt import QMessageBox
import re
import threading
reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')  

mutex = threading.Lock()    

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

def WrongA():
    reply = QMessageBox.information(None,"0xcc_","Illegal Ip!", QMessageBox.__str__("^"))
        
def Check_ip(Input_ip):
        R = reip.findall(Input_ip)
        if not R:
            a=WrongA()
            return False
        return True

    
    
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(930, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(930, 600))
        MainWindow.setMaximumSize(QtCore.QSize(930, 600))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icon/radioactive-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-image: url(:/BackGround/ws_Paper_Texture_1024x768.jpg)\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("QPushButton:{background-image: url(:/Button1/round_button_0257.jpg)}\n"
"#pushButton_1:{url(:/Button1/round_button_0257.jpg)}"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(670, 50, 101, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("Background:rgba(255, 255, 255, 0)"))
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(760, 510, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("Background: rgba(255,255,0,0)"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(834, 120, 81, 23))
        self.pushButton.setStyleSheet(_fromUtf8("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(834, 200, 81, 23))
        self.pushButton_2.setStyleSheet(_fromUtf8("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(834, 280, 81, 23))
        self.pushButton_3.setStyleSheet(_fromUtf8("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(834, 360, 81, 23))
        self.pushButton_4.setStyleSheet(_fromUtf8("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 480, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("Background:rgba(255,255,0,0)"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(550, 490, 61, 61))
        self.pushButton_5.setStyleSheet(_fromUtf8("QPushButton{Background-image:url(:/Button1/utilities-terminal-icon.png)}\n"
"#pushButton_5{image:url(:/Button1/utilities-terminal-icon.png)}"))
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 480, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("Background: rgba(255,255,0,0)"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 520, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("Background: rgba(255,255,0,0)"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(650, 110, 151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setItalic(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(_fromUtf8("Background: rgba(255,255,0,0)"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(650, 190, 151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setItalic(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(_fromUtf8("Background: rgba(255,255,0,0)"))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(650, 270, 151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setItalic(True)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(_fromUtf8("Background: rgba(255,255,0,0)"))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(650, 350, 151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setItalic(True)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet(_fromUtf8("Background: rgba(255,255,0,0)"))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 470, 161, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setItalic(True)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet(_fromUtf8("Background: rgba(255,255,0,0)"))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(140, 520, 161, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setItalic(True)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet(_fromUtf8("Background: rgba(255,255,0,0)"))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(100, 30, 451, 391))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet(_fromUtf8("Background: rgba(255,255,0,0)"))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        """Connection Start"""
        self.pushButton .clicked.connect(self.msg_pushButton_1)
        self.pushButton_2.clicked.connect(self.msg_pushButton_2)
        self.pushButton_3.clicked.connect(self.msg_pushButton_3)
        self.pushButton_4.clicked.connect(self.msg_pushButton_4)
        self.pushButton_5.clicked.connect(self.GetIpAndGateway)
        
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "0xcc_ARpAttaka", None))
        self.label.setText(_translate("MainWindow", "Target IP", None))
        self.label_2.setText(_translate("MainWindow", "Powered by 0xcc", None))
        self.pushButton.setText(_translate("MainWindow", "Attaka", None))
        self.pushButton_2.setText(_translate("MainWindow", "Attaka", None))
        self.pushButton_3.setText(_translate("MainWindow", "Attaka", None))
        self.pushButton_4.setText(_translate("MainWindow", "Attaka", None))
        self.label_3.setText(_translate("MainWindow", "Host Scan:", None))
        self.label_4.setText(_translate("MainWindow", "IP:", None))
        self.label_5.setText(_translate("MainWindow", "GateWay:", None))


         #Simple test function word.

    def msg_pushButton_1(self) :
        
        Ip_input = str(self.lineEdit.text())
        R = Check_ip(Ip_input)
        Src_ip = str(self.lineEdit_5.text())
        GateWay = str(self.lineEdit_6.text())
        
        if R:
            
            QMessageBox.information(None,"0xcc_"," Start Attacking..!",QMessageBox.__str__("_"))
            dest_IP = Ip_input
            dest_mac = "a"
            res = arp_backend.arp_resolve(dest_IP,Src_ip)
            
           
            if res:
                dest_mac = arp_backend.mac_straddr(res, 1, ":")
            else :
                QMessageBox.information(None,"0xcc_"," IP NOT FOUND!",QMessageBox.__str__("..."))
            
            Attack_thread1 = threading.Thread(target=arp_backend.StartAttack,args=(dest_IP,dest_mac,GateWay))
            Attack_thread2 = threading.Thread(target=arp_backend.StartAttack,args=(dest_IP,dest_mac,GateWay))
            """Start Attaka."""
            Attack_thread1.start()
            Attack_thread2.start()
            if arp_backend.M == False:
                QMessageBox.information(None,"0xcc_","Attaka Failed.Please install winpcap.exe(just in the package), and Run me with Administrator!",QMessageBox.__str__("..."))
        
        
    def msg_pushButton_2(self ):
        
        Ip_input = str(self.lineEdit_2.text())
        R = Check_ip(Ip_input)
        Src_ip = str(self.lineEdit_5.text())
        GateWay = str(self.lineEdit_6.text())
        
        if R:
            
            QMessageBox.information(None,"0xcc_"," Start Attacking..!",QMessageBox.__str__("_"))
            dest_IP = Ip_input
            dest_mac = "a"
            res = arp_backend.arp_resolve(dest_IP,Src_ip)
           
            if res:
                dest_mac = arp_backend.mac_straddr(res, 1, ":")
            else :
                QMessageBox.information(None,"0xcc_"," IP NOT FOUND!",QMessageBox.__str__("..."))
            
            Attack_thread1 = threading.Thread(target=arp_backend.StartAttack,args=(dest_IP,dest_mac,GateWay))
            Attack_thread2 = threading.Thread(target=arp_backend.StartAttack,args=(dest_IP,dest_mac,GateWay))
            """Start Attaka."""
            Attack_thread1.start()
            Attack_thread2.start()
            if arp_backend.M == False:
                QMessageBox.information(None,"0xcc_","Attaka Failed.Please install winpcap(in the package) and Run me with Administrator!",QMessageBox.__str__("..."))
        
                    
    def msg_pushButton_3(self ):
        
        Ip_input = str(self.lineEdit_3.text())
        R = Check_ip(Ip_input)
        Src_ip = str(self.lineEdit_5.text())
        GateWay = str(self.lineEdit_6.text())
        
        if R:
            
            QMessageBox.information(None,"0xcc_"," Start Attacking..!",QMessageBox.__str__("_"))
            dest_IP = Ip_input
            dest_mac = "a"
            res = arp_backend.arp_resolve(dest_IP,Src_ip)
            
            if res:
                dest_mac = arp_backend.mac_straddr(res, 1, ":")
            else :
                QMessageBox.information(None,"0xcc_"," IP NOT FOUND!",QMessageBox.__str__("..."))
            
            Attack_thread1 = threading.Thread(target=arp_backend.StartAttack,args=(dest_IP,dest_mac,GateWay))
            Attack_thread2 = threading.Thread(target=arp_backend.StartAttack,args=(dest_IP,dest_mac,GateWay))
            """Start Attaka."""
            Attack_thread1.start()
            Attack_thread2.start()
            
            if arp_backend.M == False:
                QMessageBox.information(None,"0xcc_","Attaka Failed.Please install winpcap(in the package) and Run me with Administrator!",QMessageBox.__str__("..."))
        
    def msg_pushButton_4(self ):
        
        Ip_input = str(self.lineEdit_4.text())
        R = Check_ip(Ip_input)
        Src_ip = str(self.lineEdit_5.text())
        GateWay = str(self.lineEdit_6.text())
        
        if R:
            
            QMessageBox.information(None,"0xcc_"," Start Attacking..!",QMessageBox.__str__("_"))
            dest_IP = Ip_input
            dest_mac = "a"
            res = arp_backend.arp_resolve(dest_IP,Src_ip)
           
            if res:
                dest_mac = arp_backend.mac_straddr(res, 1, ":")
            else :
                QMessageBox.information(None,"0xcc_"," IP NOT FOUND!",QMessageBox.__str__("..."))
            
            Attack_thread1 = threading.Thread(target=arp_backend.StartAttack,args=(dest_IP,dest_mac,GateWay))
            Attack_thread2 = threading.Thread(target=arp_backend.StartAttack,args=(dest_IP,dest_mac,GateWay))
            """Start Attaka."""
            Attack_thread1.start()
            Attack_thread2.start()
            if arp_backend.M == False:
                QMessageBox.information(None,"0xcc_","Attaka Failed.Please install winpcap(in the package) and Run me with Administrator!",QMessageBox.__str__("..."))
        
            
    def GetIpAndGateway(self):
        
        self.listWidget.clear()
            
        """Get 2 elem.""" 
        
        Ip_input = str(self.lineEdit_5.text())
        GateWay = str(self.lineEdit_6.text())
        Ip_CHECK = Check_ip(Ip_input)
        GateWay_CHECK = Check_ip(GateWay)
        #Get two Fundamental parameter.
        if Ip_CHECK and GateWay_CHECK :
            
            IP = Ip_input
            Gate_ = GateWay
            #Substitute with a process_bar.
            QMessageBox.information(None,"0xcc_"," Scan Started! Please Wait...",QMessageBox.__str__('^_^'))
            #Substitute with a process_bar. 
            
            def ProcessA(dest_ip,src_ip=IP,Gate=Gate_):
                res = arp_backend.arp_resolve(dest_ip, src_ip)
                #Host Online.
                if res:
                    mac = arp_backend.mac_straddr(res, 1, ":")
                    try :
                        hostname = arp_backend.socket.gethostbyaddr(dest_ip)
                        hostname=hostname[0]
                    except:
                        if dest_ip == Gate_:
                            hostname = "NetWork Router"
                        else:
                            hostname = "Android platform Or Family Router."
                    if mutex.acquire():
                        self.listWidget.addItem("Hostname:")
                        self.listWidget.addItem(hostname)
                        self.listWidget.addItem("IP:"+" "+dest_ip+"-- MAC:"+mac)
                        mutex.release()
            #QMessageBox.information(None,"0xcc_"," Launch Scan!",QMessageBox.__str__("_"))
          
            
            threadpool = []
            num = 0
            wait =0
            Scan_List = arp_backend.ip_process(str(IP)) 
            #20 Threads.
            for x in Scan_List:
                t = threading.Thread(target=ProcessA,args=(str(x),))
                threadpool.append(t)
            for th in threadpool:
                if wait > 8:
                    time.sleep(1)
                    wait = 0
                th.start()
                wait +=1
         
      
"""
def Wait_Dialog():
    
    Process_Dialog = QtGui.QProgressDialog()
    
    Process_Dialog.setWindowTitle("0xcc")
    Process_Dialog.autoFillBackground()
    x=300
    while x>0:
        
        Process_Dialog.show()
        x-=1
    #Stimulated.
""" 

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

