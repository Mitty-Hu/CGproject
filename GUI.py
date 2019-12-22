import cv2

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5 import QtCore,QtGui, QtWidgets
from PyQt5.QtCore import QDir,pyqtSlot
from GUIDesign import *

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.CameraTimer = QtCore.QTimer()

        self.CAM_NUM = 0
        self.Gender = -1
        self.VideoMode = 0

        self.EdgeTractThrehold1 = 50
        self.EdgeTractThrehold2 = 101

        self.report = "testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest"

        self.setupUi(self)
        self.slot_init()


    def slot_init(self):
        self.button_CaptureAnalyse.clicked.connect(self.CaptureAnalyse)
        self.CameraTimer.timeout.connect(self.ShowCamera)#每次倒计时溢出，调用函数刷新页面
        self.actionOpenImage.triggered.connect(self.OpenImage)
        self.actionOpenCamera.triggered.connect(self.OpenCamera)
        self.actionCloseCamera.triggered.connect(self.CloseCamera)
        self.actionClearImage.triggered.connect(self.ClearImage)
        self.horizontalSlider_EdgeTract.valueChanged.connect(self.SliderChangeValue)

    def OpenCamera(self):#打开摄像头，启动倒计时
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 后一个参数用来消一个奇怪的warn
        if self.CameraTimer.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self,'warning',"请检查摄像头与电脑是否连接正确",buttons=QtWidgets.QMessageBox.Ok)
            else:
                self.CameraTimer.start(30)
        else:
            self.CameraTimer.stop()
            self.cap.release()
            self.label_ShowCamera.clear()

    def ShowCamera(self):
        if self.radioButton_NormalImage.isChecked():
            self.VideoMode = 0
        elif self.radioButton_EdgeTract.isChecked():
            self.VideoMode = 2
        elif self.radioButton_FaceTract.isChecked():
            self.VideoMode = 1

        flag, self.image = self.cap.read()

        if self.VideoMode == 0:
            ShowVideo = cv2.resize(self.image, (880, 495))
        elif self.VideoMode == 2:
            self.edge = cv2.Canny(self.image,self.EdgeTractThrehold1,self.EdgeTractThrehold2)
            ShowVideo = cv2.resize(self.edge, (880,495))

        ShowVideo = cv2.cvtColor(ShowVideo, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(ShowVideo.data, ShowVideo.shape[1], ShowVideo.shape[0],
                                 QtGui.QImage.Format_RGB888)
        self.label_ShowCamera.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def CloseCamera(self):
        self.CameraTimer.stop()
        self.cap.release()
        self.label_ShowCamera.clear()
        self.label_ShowCamera.setPixmap(QtGui.QPixmap("background.png"))

    def CaptureAnalyse(self):#要思考未打开摄像头时按下“拍照”的问题
        if self.radioButton_Male.isChecked():
            self.Gender = 1
        elif self.radioButton_Female.isChecked():
            self.Gender = 0

        if self.Gender == -1:
            msgGender = QtWidgets.QMessageBox.warning(self, 'warning', "请选择性别", buttons=QtWidgets.QMessageBox.Ok)
        else:
            flag, self.image = self.cap.read()
            ShowCapture = cv2.resize(self.image, (880,495))
            ShowCapture = cv2.cvtColor(ShowCapture, cv2.COLOR_BGR2RGB)
            showImage = QtGui.QImage(ShowCapture.data, ShowCapture.shape[1], ShowCapture.shape[0],
                                    QtGui.QImage.Format_RGB888)
            self.label_ShowCamera.setPixmap(QtGui.QPixmap.fromImage(showImage))
            self.CameraTimer.stop()
            self.textEdit_Report.setPlainText(self.report)

    def OpenImage(self):
        curPath = QDir.currentPath()
        imgName,imgType = QFileDialog.getOpenFileName(self,"打开图片",curPath," *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
        print(imgName)
        img = QtGui.QPixmap(imgName).scaled(self.label_ShowCamera.width(), self.label_ShowCamera.height())
        self.label_ShowCamera.setPixmap(img)

    def ClearImage(self):
        self.CameraTimer.stop()
        self.cap.release()
        self.label_ShowCamera.clear()
        self.textEdit_Report.clear()

    def SliderChangeValue(self):
        self.EdgeTractThrehold2 = self.horizontalSlider_EdgeTract.value()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())