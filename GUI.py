import cv2

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5 import QtCore,QtGui,QtWidgets
from GUIDesign import *

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.CameraTimer = QtCore.QTimer()

        self.CAM_NUM = 0

        self.setupUi(self)
        self.slot_init()

    def slot_init(self):
        self.button_OpenCamera.clicked.connect(self.OpenCamera)
        self.button_CloseCamera.clicked.connect(self.CloseCamera)
        self.button_Capture.clicked.connect(self.Capture)
        self.CameraTimer.timeout.connect(self.ShowCamera)#每次倒计时溢出，调用函数刷新页面
        self.button_OpenImage.clicked.connect(self.OpenImage)

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
        flag, self.image = self.cap.read()

        ShowVideo = cv2.resize(self.image, (560, 315))
        ShowVideo = cv2.cvtColor(ShowVideo, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(ShowVideo.data, ShowVideo.shape[1], ShowVideo.shape[0],
                                 QtGui.QImage.Format_RGB888)
        self.label_ShowCamera.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def CloseCamera(self):
        self.CameraTimer.stop()
        self.cap.release()
        self.label_ShowCamera.clear()
        self.label_ShowCamera.setPixmap(QtGui.QPixmap("background.png"))

    def Capture(self):#要思考未打开摄像头时按下“拍照”的问题
        flag, self.image = self.cap.read()
        ShowCapture = cv2.resize(self.image, (560, 315))
        ShowCapture = cv2.cvtColor(ShowCapture, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(ShowCapture.data, ShowCapture.shape[1], ShowCapture.shape[0],
                                 QtGui.QImage.Format_RGB888)
        self.label_ShowCamera.setPixmap(QtGui.QPixmap.fromImage(showImage))
        self.CameraTimer.stop()
        self.cap.release()

    def OpenImage(self):
        imgName,imgType = QFileDialog.getOpenFileName(self,"打开图片",""," *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
        print(imgName)
        png = QtGui.QPixmap(imgName).scaled(self.label_ShowCamera.width(), self.label_ShowCamera.height())
        self.label_ShowCamera.setPixmap(png)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())