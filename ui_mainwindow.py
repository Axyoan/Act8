# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 609)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.spinBox_green = QSpinBox(self.groupBox)
        self.spinBox_green.setObjectName(u"spinBox_green")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        self.spinBox_green.setFont(font)
        self.spinBox_green.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_green, 7, 3, 1, 1)

        self.line_id = QLineEdit(self.groupBox)
        self.line_id.setObjectName(u"line_id")
        self.line_id.setFont(font)

        self.gridLayout.addWidget(self.line_id, 0, 3, 1, 1)

        self.btnCreate_back = QPushButton(self.groupBox)
        self.btnCreate_back.setObjectName(u"btnCreate_back")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(16)
        self.btnCreate_back.setFont(font1)

        self.gridLayout.addWidget(self.btnCreate_back, 11, 1, 1, 3)

        self.lbl_yDestination = QLabel(self.groupBox)
        self.lbl_yDestination.setObjectName(u"lbl_yDestination")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        self.lbl_yDestination.setFont(font2)
        self.lbl_yDestination.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_yDestination, 4, 1, 1, 2)

        self.spinBox_xOrigin = QSpinBox(self.groupBox)
        self.spinBox_xOrigin.setObjectName(u"spinBox_xOrigin")
        self.spinBox_xOrigin.setFont(font)
        self.spinBox_xOrigin.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_xOrigin, 1, 3, 1, 1)

        self.spinBox_yOrigin = QSpinBox(self.groupBox)
        self.spinBox_yOrigin.setObjectName(u"spinBox_yOrigin")
        self.spinBox_yOrigin.setFont(font)
        self.spinBox_yOrigin.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_yOrigin, 2, 3, 1, 1)

        self.lbl_id = QLabel(self.groupBox)
        self.lbl_id.setObjectName(u"lbl_id")
        self.lbl_id.setFont(font2)
        self.lbl_id.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_id, 0, 1, 1, 1)

        self.lbl_velocity_5 = QLabel(self.groupBox)
        self.lbl_velocity_5.setObjectName(u"lbl_velocity_5")
        self.lbl_velocity_5.setFont(font2)
        self.lbl_velocity_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_velocity_5, 8, 1, 1, 1)

        self.spinBox_yDestination = QSpinBox(self.groupBox)
        self.spinBox_yDestination.setObjectName(u"spinBox_yDestination")
        self.spinBox_yDestination.setFont(font)
        self.spinBox_yDestination.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_yDestination, 4, 3, 1, 1)

        self.lbl_velocity_4 = QLabel(self.groupBox)
        self.lbl_velocity_4.setObjectName(u"lbl_velocity_4")
        self.lbl_velocity_4.setFont(font2)
        self.lbl_velocity_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_velocity_4, 7, 1, 1, 1)

        self.spinBox_red = QSpinBox(self.groupBox)
        self.spinBox_red.setObjectName(u"spinBox_red")
        self.spinBox_red.setFont(font)
        self.spinBox_red.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_red, 6, 3, 1, 1)

        self.spinBox_xDestination = QSpinBox(self.groupBox)
        self.spinBox_xDestination.setObjectName(u"spinBox_xDestination")
        self.spinBox_xDestination.setFont(font)
        self.spinBox_xDestination.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_xDestination, 3, 3, 1, 1)

        self.lbl_xOrigin = QLabel(self.groupBox)
        self.lbl_xOrigin.setObjectName(u"lbl_xOrigin")
        self.lbl_xOrigin.setFont(font2)
        self.lbl_xOrigin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_xOrigin, 1, 1, 1, 2)

        self.line_velocity = QLineEdit(self.groupBox)
        self.line_velocity.setObjectName(u"line_velocity")
        self.line_velocity.setFont(font)

        self.gridLayout.addWidget(self.line_velocity, 5, 3, 1, 1)

        self.spinBox_blue = QSpinBox(self.groupBox)
        self.spinBox_blue.setObjectName(u"spinBox_blue")
        self.spinBox_blue.setFont(font)
        self.spinBox_blue.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_blue, 8, 3, 1, 1)

        self.lbl_velocity_3 = QLabel(self.groupBox)
        self.lbl_velocity_3.setObjectName(u"lbl_velocity_3")
        self.lbl_velocity_3.setFont(font2)
        self.lbl_velocity_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_velocity_3, 6, 1, 1, 1)

        self.lbl_xDestination = QLabel(self.groupBox)
        self.lbl_xDestination.setObjectName(u"lbl_xDestination")
        self.lbl_xDestination.setFont(font2)
        self.lbl_xDestination.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_xDestination, 3, 1, 1, 2)

        self.lbl_velocity = QLabel(self.groupBox)
        self.lbl_velocity.setObjectName(u"lbl_velocity")
        self.lbl_velocity.setFont(font2)
        self.lbl_velocity.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_velocity, 5, 1, 1, 2)

        self.lbl_yOrigin = QLabel(self.groupBox)
        self.lbl_yOrigin.setObjectName(u"lbl_yOrigin")
        self.lbl_yOrigin.setFont(font2)
        self.lbl_yOrigin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_yOrigin, 2, 1, 1, 2)

        self.btnCreate_front = QPushButton(self.groupBox)
        self.btnCreate_front.setObjectName(u"btnCreate_front")
        self.btnCreate_front.setFont(font1)

        self.gridLayout.addWidget(self.btnCreate_front, 10, 1, 1, 3)

        self.btn_show = QPushButton(self.groupBox)
        self.btn_show.setObjectName(u"btn_show")
        self.btn_show.setFont(font1)

        self.gridLayout.addWidget(self.btn_show, 12, 1, 1, 3)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.plainText = QPlainTextEdit(self.centralwidget)
        self.plainText.setObjectName(u"plainText")
        self.plainText.setFont(font2)

        self.gridLayout_2.addWidget(self.plainText, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 850, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Actividad 8", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.btnCreate_back.setText(QCoreApplication.translate("MainWindow", u"Agregar final", None))
        self.lbl_yDestination.setText(QCoreApplication.translate("MainWindow", u"Destino en Y:", None))
        self.lbl_id.setText(QCoreApplication.translate("MainWindow", u"id:", None))
        self.lbl_velocity_5.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lbl_velocity_4.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lbl_xOrigin.setText(QCoreApplication.translate("MainWindow", u"Origen en X:", None))
        self.lbl_velocity_3.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lbl_xDestination.setText(QCoreApplication.translate("MainWindow", u"Destino en X:", None))
        self.lbl_velocity.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.lbl_yOrigin.setText(QCoreApplication.translate("MainWindow", u"Origen en Y:", None))
        self.btnCreate_front.setText(QCoreApplication.translate("MainWindow", u"Agregar inicio", None))
        self.btn_show.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

