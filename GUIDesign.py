# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIDesign.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(290, 20, 20, 381))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_ShowCamera = QtWidgets.QLabel(self.centralwidget)
        self.label_ShowCamera.setGeometry(QtCore.QRect(340, 90, 400, 225))
        self.label_ShowCamera.setText("")
        self.label_ShowCamera.setObjectName("label_ShowCamera")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 90, 221, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_OpenCamera = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_OpenCamera.setFont(font)
        self.button_OpenCamera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_OpenCamera.setMouseTracking(False)
        self.button_OpenCamera.setObjectName("button_OpenCamera")
        self.verticalLayout.addWidget(self.button_OpenCamera)
        self.button_Capture = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_Capture.setFont(font)
        self.button_Capture.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_Capture.setMouseTracking(False)
        self.button_Capture.setObjectName("button_Capture")
        self.verticalLayout.addWidget(self.button_Capture)
        self.button_CloseCamera = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_CloseCamera.setFont(font)
        self.button_CloseCamera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_CloseCamera.setMouseTracking(False)
        self.button_CloseCamera.setObjectName("button_CloseCamera")
        self.verticalLayout.addWidget(self.button_CloseCamera)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.button_OpenCamera.clicked.connect(self.label_ShowCamera.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Facial health"))
        self.button_OpenCamera.setText(_translate("MainWindow", "开启摄像头"))
        self.button_Capture.setText(_translate("MainWindow", "拍照"))
        self.button_CloseCamera.setText(_translate("MainWindow", "关闭摄像头"))
