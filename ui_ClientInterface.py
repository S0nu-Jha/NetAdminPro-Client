# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ClientInterfaceLdqPwq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ClientResources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1022, 731)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-image: url(:/images/images/BgClient.jpg);\n"
"}\n"
"\n"
"#widget{\n"
"	background-color: rgb(9, 27, 68);\n"
"	border-radius:20px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(9, 10, 37);\n"
"	padding: 5px 3px;\n"
"	border-radius:5px;\n"
"	\n"
"}\n"
"QPushButton{\n"
"	background-color:  rgb(9, 10, 37);\n"
"	padding: 10px 5px;\n"
"	border-radius:5px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(400, 700))
        self.widget.setMaximumSize(QSize(400, 700))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.InformationPage = QWidget()
        self.InformationPage.setObjectName(u"InformationPage")
        self.verticalLayout_3 = QVBoxLayout(self.InformationPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.InfoLogo = QLabel(self.InformationPage)
        self.InfoLogo.setObjectName(u"InfoLogo")
        self.InfoLogo.setPixmap(QPixmap(u":/icons/icons/airplay.png"))

        self.verticalLayout_3.addWidget(self.InfoLogo, 0, Qt.AlignHCenter)

        self.InfoText2 = QLabel(self.InformationPage)
        self.InfoText2.setObjectName(u"InfoText2")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.InfoText2.setFont(font)

        self.verticalLayout_3.addWidget(self.InfoText2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.InfoText = QLabel(self.InformationPage)
        self.InfoText.setObjectName(u"InfoText")

        self.verticalLayout_3.addWidget(self.InfoText, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.UserInputInfo = QFrame(self.InformationPage)
        self.UserInputInfo.setObjectName(u"UserInputInfo")
        self.UserInputInfo.setFrameShape(QFrame.StyledPanel)
        self.UserInputInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.UserInputInfo)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.PcName = QLineEdit(self.UserInputInfo)
        self.PcName.setObjectName(u"PcName")

        self.verticalLayout_4.addWidget(self.PcName)

        self.InfoClientIpAddr = QLineEdit(self.UserInputInfo)
        self.InfoClientIpAddr.setObjectName(u"InfoClientIpAddr")

        self.verticalLayout_4.addWidget(self.InfoClientIpAddr)

        self.InfoServerIpAddr = QLineEdit(self.UserInputInfo)
        self.InfoServerIpAddr.setObjectName(u"InfoServerIpAddr")

        self.verticalLayout_4.addWidget(self.InfoServerIpAddr)

        self.InfoServerPort = QLineEdit(self.UserInputInfo)
        self.InfoServerPort.setObjectName(u"InfoServerPort")

        self.verticalLayout_4.addWidget(self.InfoServerPort)


        self.verticalLayout_3.addWidget(self.UserInputInfo)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.InfoCheckBox = QCheckBox(self.InformationPage)
        self.InfoCheckBox.setObjectName(u"InfoCheckBox")

        self.verticalLayout_3.addWidget(self.InfoCheckBox)

        self.InfoConnectBTn = QPushButton(self.InformationPage)
        self.InfoConnectBTn.setObjectName(u"InfoConnectBTn")

        self.verticalLayout_3.addWidget(self.InfoConnectBTn, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.InfoConnectIssueBtn = QPushButton(self.InformationPage)
        self.InfoConnectIssueBtn.setObjectName(u"InfoConnectIssueBtn")
        font1 = QFont()
        font1.setUnderline(True)
        self.InfoConnectIssueBtn.setFont(font1)

        self.verticalLayout_3.addWidget(self.InfoConnectIssueBtn, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.InfoCC = QLabel(self.InformationPage)
        self.InfoCC.setObjectName(u"InfoCC")

        self.verticalLayout_3.addWidget(self.InfoCC, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.InformationPage)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NetAdminPro Client", None))
        self.InfoLogo.setText("")
        self.InfoText2.setText(QCoreApplication.translate("MainWindow", u"Connect Your PC To Server", None))
        self.InfoText.setText(QCoreApplication.translate("MainWindow", u"Enter Your Information Below", None))
        self.PcName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter PC Name", None))
        self.InfoClientIpAddr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter I.P. Address Of Client", None))
        self.InfoServerIpAddr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter The I.P. Address Of Server", None))
        self.InfoServerPort.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter The Port Number Of Server", None))
        self.InfoCheckBox.setText(QCoreApplication.translate("MainWindow", u"Are The Above Information Correct", None))
        self.InfoConnectBTn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.InfoConnectIssueBtn.setText(QCoreApplication.translate("MainWindow", u"Click Here If Facing issue To Connect", None))
        self.InfoCC.setText(QCoreApplication.translate("MainWindow", u"CC Anjani Jha", None))
    # retranslateUi

