# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QWidget)


class Ui_vtn_principal(object):
    def __init__(self):
        self.stb_estado = None
        self.txt_apellido = None
        self.txt_nombre = None
        self.cb_tipo_persona = None
        self.btn_grabar = None
        self.lineEdit_3 = None

    def setupUi(self, vtn_principal):
        if not vtn_principal.objectName():
            vtn_principal.setObjectName(u"Dialog")
        vtn_principal.resize(369, 303)
        self.label = QLabel(vtn_principal)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 30, 47, 13))
        self.label_2 = QLabel(vtn_principal)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 70, 47, 13))
        self.label_3 = QLabel(vtn_principal)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 110, 47, 13))
        self.label_4 = QLabel(vtn_principal)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 150, 47, 13))
        self.label_5 = QLabel(vtn_principal)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 190, 47, 13))
        self.comboBox = QComboBox(vtn_principal)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(160, 30, 111, 22))
        self.pushButton = QPushButton(vtn_principal)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 240, 75, 23))
        self.lineEdit = QLineEdit(vtn_principal)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 70, 113, 20))
        self.lineEdit.setMaxLength(50)
        self.lineEdit_2 = QLineEdit(vtn_principal)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(160, 110, 113, 20))
        self.lineEdit_2.setMaxLength(50)
        self.lineEdit_3 = QLineEdit(vtn_principal)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(160, 150, 113, 20))
        self.lineEdit_3.setMaxLength(10)
        self.lineEdit_4 = QLineEdit(vtn_principal)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(160, 190, 113, 20))
        self.lineEdit_4.setMaxLength(100)

        self.retranslateUi(vtn_principal)

        QMetaObject.connectSlotsByName(vtn_principal)

    # setupUi

    def retranslateUi(self, vtn_principal):
        vtn_principal.setWindowTitle(QCoreApplication.translate("vtn_principal", u"Ventana Principal", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Tipo:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nombre:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Apellido:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Cedula:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Correo;", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Estudiante", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Docente", None))

        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Grabar", None))
    # retranslateUi
