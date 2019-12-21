# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChildDialog_SelectGender.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChildDialog_SelectGender(object):
    def setupUi(self, ChildDialog_SelectGender):
        ChildDialog_SelectGender.setObjectName("ChildDialog_SelectGender")
        ChildDialog_SelectGender.resize(338, 226)
        self.verticalLayoutWidget = QtWidgets.QWidget(ChildDialog_SelectGender)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 40, 211, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_SelectGender = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_SelectGender.setObjectName("label_SelectGender")
        self.verticalLayout.addWidget(self.label_SelectGender)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_Male = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_Male.setObjectName("button_Male")
        self.horizontalLayout.addWidget(self.button_Male)
        self.button_Female = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_Female.setObjectName("button_Female")
        self.horizontalLayout.addWidget(self.button_Female)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ChildDialog_SelectGender)
        QtCore.QMetaObject.connectSlotsByName(ChildDialog_SelectGender)

    def retranslateUi(self, ChildDialog_SelectGender):
        _translate = QtCore.QCoreApplication.translate
        ChildDialog_SelectGender.setWindowTitle(_translate("ChildDialog_SelectGender", "性别选择"))
        self.label_SelectGender.setText(_translate("ChildDialog_SelectGender", "请选择你的性别："))
        self.button_Male.setText(_translate("ChildDialog_SelectGender", "男"))
        self.button_Female.setText(_translate("ChildDialog_SelectGender", "女"))
