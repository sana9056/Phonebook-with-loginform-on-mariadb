from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import database

"""
Скрипт добавления контактов
Здесь ничего трогать не нужно
#sana9056
"""
class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def add_contact(self):
        select_name, select_phone, select_date = None, None, None
        try:
            database.cur.execute(f"SELECT name FROM contacts WHERE name = '{self.name.text()}' "
                              f"and phone = '{self.number_phone.text()}'"
                              f" and date = '{self.date.text()}'")
            select_name = database.cur.fetchone()[0]
            database.cur.execute(f"SELECT phone FROM contacts WHERE name = '{self.name.text()}' "
                              f"and phone = '{self.number_phone.text()}'"
                              f" and (SELECT DATE_FORMAT(date, '%Y-%m-%d') FROM contacts WHERE name = '{self.name.text()}' "
                              f"and phone = '{self.number_phone.text()}') = '{self.date.text()}'")
            select_phone = str(database.cur.fetchone()[0])
            database.cur.execute(f"SELECT date FROM contacts WHERE name = '{self.name.text()}' "
                              f"and phone = '{self.number_phone.text()}'"
                              f" and (SELECT DATE_FORMAT(date, '%Y-%m-%d') FROM contacts WHERE name = '{self.name.text()}' "
                              f"and phone = '{self.number_phone.text()}') = '{self.date.text()}'")
            select_date = database.cur.fetchone()[0]
        except:
            pass

        if self.name.text() != select_name and self.number_phone.text() != select_phone and self.date.text() != select_date:
            database.add_data(self.name.text(), self.number_phone.text(), self.date.text())
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setIcon(QMessageBox.Information)
            if self.name.text()[0] == 'А' or self.name.text()[0] == 'Б':
                msg.setText("Контакт добавлен во вкладку АБ")
            elif self.name.text()[0] == 'В' or self.name.text()[0] == 'Г':
                msg.setText("Контакт добавлен во вкладку ВГ")
            elif self.name.text()[0] == 'Д' or self.name.text()[0] == 'Е':
                msg.setText("Контакт добавлен во вкладку ДЕ")
            elif self.name.text()[0] == 'Ж' or self.name.text()[0] == 'З'\
                    or self.name.text()[0] == 'И' or self.name.text()[0] == 'Й':
                msg.setText("Контакт добавлен во вкладку ЖЗИЙ")
            elif self.name.text()[0] == 'К' or self.name.text()[0] == 'Л':
                msg.setText("Контакт добавлен во вкладку КЛ")
            elif self.name.text()[0] == 'М' or self.name.text()[0] == 'Н':
                msg.setText("Контакт добавлен во вкладку МН")
            elif self.name.text()[0] == 'О' or self.name.text()[0] == 'П':
                msg.setText("Контакт добавлен во вкладку ОП")
            elif self.name.text()[0] == 'Р' or self.name.text()[0] == 'С':
                msg.setText("Контакт добавлен во вкладку РС")
            elif self.name.text()[0] == 'Т' or self.name.text()[0] == 'У':
                msg.setText("Контакт добавлен во вкладку ТУ")
            elif self.name.text()[0] == 'Ф' or self.name.text()[0] == 'Х':
                msg.setText("Контакт добавлен во вкладку ФХ")
            elif self.name.text()[0] == 'Ц' or self.name.text()[0] == 'Ч'\
                    or self.name.text()[0] == 'Ш' or self.name.text()[0] == 'Щ':
                msg.setText("Контакт добавлен во вкладку ЦЧШЩ")
            elif self.name.text()[0] == 'Ъ' or self.name.text()[0] == 'Ы'\
                    or self.name.text()[0] == 'Ь' or self.name.text()[0] == 'Э':
                msg.setText("Контакт добавлен во вкладку ЪЫЬЭ")
            elif self.name.text()[0] == 'Ю' or self.name.text()[0] == 'Я':
                msg.setText("Контакт добавлен во вкладку ЮЯ")
            else:
                msg.setText("Контакт добавлен")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Контакт с такими данными уже существует")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(550, 250))
        Form.setMaximumSize(QtCore.QSize(550, 250))
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(140, 150, 241, 64))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.add = QtWidgets.QPushButton(self.splitter)
        self.add.setMinimumSize(118, 61)
        self.add.setMaximumSize(118, 61)
        self.add.setObjectName("add")
        self.cancel = QtWidgets.QPushButton(self.splitter)
        self.cancel.setMinimumSize(118, 61)
        self.cancel.setMaximumSize(118, 61)
        self.cancel.setObjectName("cancel")
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(110, 50, 321, 85))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.name = QtWidgets.QLineEdit(self.splitter_2)
        self.name.setMinimumSize(321, 24)
        self.name.setMaximumSize(321, 24)
        self.name.setObjectName("name")
        self.number_phone = QtWidgets.QLineEdit(self.splitter_2)
        self.number_phone.setMinimumSize(321, 24)
        self.number_phone.setMaximumSize(321, 24)
        self.number_phone.setObjectName("number_phone")
        self.date = QtWidgets.QDateEdit(self.splitter_2)
        self.date.setMinimumSize(321, 25)
        self.date.setMaximumSize(321, 25)
        self.date.setObjectName("date")
        self.date.setCalendarPopup(True)
        self.add.clicked.connect(self.add_contact)
        self.cancel.clicked.connect(self.close)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add.setText(_translate("Form", "Добавить"))
        self.cancel.setText(_translate("Form", "Отмена"))
        self.name.setPlaceholderText(_translate("Form", "Имя пользователя"))
        self.number_phone.setPlaceholderText(_translate("Form", "Телефон"))
        self.date.setDisplayFormat(_translate("Form", "yyyy-MM-dd"))
