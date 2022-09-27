from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import database
from phonebook import Ui_Form as Ui_book
import main_window

"""
Скрипты регистрации.
Здесь ничего трогать не нужно
#sana9056
"""
class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def reg_user(self):
        if self.lineEdit.text() and self.lineEdit_2.text() and \
                self.lineEdit_2.text() == self.lineEdit_3.text():
            database.reg_user(self.lineEdit.text(), self.lineEdit_2.text(),
                                                      self.dateEdit_2.text())

            self.close()
            self._new = Ui_book()
            self._new.show()

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Неверно введены данные")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    def open_main(self):
        self.close()
        self._new = main_window.window()
        self._new.show()

    def setupUi(self, Form):
        self._new = None
        Form.setObjectName("Form")
        Form.resize(350, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(350, 250))
        Form.setMaximumSize(QtCore.QSize(350, 250))
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 60, 181, 143))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setAcceptDrops(True)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setEnabled(True)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_2.setAcceptDrops(True)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setEnabled(True)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_3.setAcceptDrops(True)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit_2.setWrapping(False)
        self.dateEdit_2.setFrame(True)
        self.dateEdit_2.setReadOnly(False)
        self.dateEdit_2.setAccelerated(False)
        self.dateEdit_2.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.dateEdit_2.setKeyboardTracking(False)
        self.dateEdit_2.setProperty("showGroupSeparator", False)
        self.dateEdit_2.setMaximumTime(QtCore.QTime(23, 59, 58))
        self.dateEdit_2.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setDate(QtCore.QDate(2000, 1, 1))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_2.setDisplayFormat("yyyy-MM-dd")
        self.verticalLayout_2.addWidget(self.dateEdit_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_2.clicked.connect(self.open_main)
        self.pushButton.clicked.connect(self.reg_user)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Имя пользователя"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Пароль"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Повторить пароль"))
        self.pushButton.setText(_translate("Form", "ОК"))
        self.pushButton_2.setText(_translate("Form", "Отмена"))
