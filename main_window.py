from PyQt5 import QtCore, QtGui, QtWidgets
from password_rec import Ui_Form
import registration
from PyQt5.QtWidgets import QMessageBox
import database
import phonebook

"""
Основной файл для работы инструмента.
Здесь ничего трогать не нужно
#sana9056
"""
class window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def open_password_rec(self):
        self._new = Ui_Form()
        self._new.show()

    def registr(self):
        self.close()
        self._new = registration.Ui_Form()
        self._new.show()

    def cash(self):
        if self.checkBox_2.isChecked() == True:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def login(self):
        database.cur.execute(f"SELECT name, password FROM users WHERE name = '{self.lineEdit.text()}' "
                          f"AND password = '{self.lineEdit_2.text()}'")
        count = 0
        for name, password in database.cur:
            if self.lineEdit.text() == name and self.lineEdit_2.text() == password:
                count = 1
                self.close()
                self._new = phonebook.Ui_Form()
                self._new.show()
        if count == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Неверно введены данные")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    def auto_login(self):
        if self.checkBox.isChecked() == True:
            database.cur.execute(f"UPDATE users SET remember_me = 1 WHERE name = '{self.lineEdit.text()}' "
                              f"AND password = '{self.lineEdit_2.text()}'")
            database.conn.commit()
            database.cur.execute(f"UPDATE users SET remember_me = 0 WHERE name <> '{self.lineEdit.text()}' "
                              f"AND password <> '{self.lineEdit_2.text()}'")
            database.conn.commit()

    def setupUi(self, Form):
        self._new = None
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(500, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(500, 300))
        Form.setMaximumSize(QtCore.QSize(500, 300))
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.password_rec = QtWidgets.QPushButton(Form)
        self.password_rec.setGeometry(QtCore.QRect(190, 250, 91, 23))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.password_rec.setFont(font)
        self.password_rec.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.password_rec.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password_rec.setFlat(True)
        self.password_rec.setObjectName("password_rec")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(110, 40, 271, 71))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
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
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(180, 180, 121, 51))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.widget1)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(80, 120, 331, 51))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Enter = QtWidgets.QPushButton(self.widget2)
        self.Enter.setObjectName("Enter")
        self.Enter.setDefault(True)
        self.horizontalLayout.addWidget(self.Enter)
        self.registration = QtWidgets.QPushButton(self.widget2)
        self.registration.setObjectName("registration")
        self.horizontalLayout.addWidget(self.registration)
        self.cancel = QtWidgets.QPushButton(self.widget2)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.retranslateUi(Form)
        database.cur.execute("SELECT name, password, remember_me FROM users WHERE remember_me = '1'")
        for name, password, remember_me in database.cur:
            if remember_me == 1:
                self.lineEdit.setText(name)
                self.lineEdit_2.setText(password)
        self.password_rec.clicked.connect(self.open_password_rec)
        self.registration.clicked.connect(self.registr)
        self.cancel.clicked.connect(self.close)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.checkBox_2.stateChanged.connect(self.cash)
        self.Enter.clicked.connect(self.login)
        self.checkBox.stateChanged.connect(self.auto_login)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.password_rec.setText(_translate("Form", "Забыли пароль?"))
        self.lineEdit.setPlaceholderText(_translate("Form", "имя пользователя"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "пароль"))
        self.checkBox.setText(_translate("Form", "Запомнить меня"))
        self.checkBox_2.setText(_translate("Form", "Показать пароль"))
        self.Enter.setText(_translate("Form", "Войти"))
        self.registration.setText(_translate("Form", "Регистрация"))
        self.cancel.setText(_translate("Form", "Отмена"))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    gui = window()
    gui.show()
    app.exec_()
