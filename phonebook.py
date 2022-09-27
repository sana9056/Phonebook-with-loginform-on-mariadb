from PyQt5 import QtCore, QtGui, QtWidgets
import add_contact
import database
import datetime
from PyQt5.QtWidgets import QMessageBox
"""
Скрипты для работы с телефонной книжкой. Отрисовка, добавление, удаление, сортировка и тп.
Здесь ничего трогать не нужно
#sana9056
"""

class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def add_contact(self):
        self._new = add_contact.Ui_Form()
        self._new.show()

    def update_table(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(13)
        database.cur.execute("SELECT name, phone, date FROM contacts")
        count = 0
        for name, phone, date in database.cur:
            if count > 12:
                self.tableWidget.insertRow(count)
            item = QtWidgets.QTableWidgetItem()
            item.setText(f"{name}")
            self.tableWidget.setItem(count, 0, item)
            item_2 = QtWidgets.QTableWidgetItem()
            item_2.setText(f"{phone}")
            self.tableWidget.setItem(count, 1, item_2)
            item_3 = QtWidgets.QTableWidgetItem()
            item_3.setText(f"{date}")
            self.tableWidget.setItem(count, 2, item_3)
            count += 1
        database.cur.execute("SELECT name, date FROM contacts")
        timenow = datetime.datetime.now() + datetime.timedelta(days=7)
        for name, date in database.cur:
            date_ = datetime.datetime(year=datetime.date.today().year, month=date.month, day=date.day)
            if datetime.datetime.now() <= date_ <= timenow:
                self.birth_names.append(f"{name} - {date}\n")
        msg = QMessageBox()
        msg.setWindowTitle("Уведомление")
        birth_names = (''.join(self.birth_names))
        msg.setText("Ближайшие дни рождения у \n"
                    f"{birth_names}")
        msg.exec_()

    def sorting_filter(self, filt):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(13)
        database.cur.execute(filt)
        count = 0
        for name, phone, date in database.cur:
            if count > 12:
                self.tableWidget.insertRow(count)
            item = QtWidgets.QTableWidgetItem()
            item.setText(f"{name}")
            self.tableWidget.setItem(count, 0, item)
            item_2 = QtWidgets.QTableWidgetItem()
            item_2.setText(f"{phone}")
            self.tableWidget.setItem(count, 1, item_2)
            item_3 = QtWidgets.QTableWidgetItem()
            item_3.setText(f"{date}")
            self.tableWidget.setItem(count, 2, item_3)
            count += 1

    def sorting(self):
        if self.pushButton.hasFocus():
            self.filt = f"SELECT name, phone, date FROM contacts WHERE name LIKE 'А%' OR name LIKE 'Б%'"
            self.sorting_filter(self.filt)
        elif self.pushButton_2.hasFocus():
            self.filt = f"SELECT name, phone, date FROM contacts WHERE name LIKE 'В%' OR name LIKE 'Г%'"
            self.sorting_filter(self.filt)
        elif self.pushButton_3.hasFocus():
            self.filt = f"SELECT name, phone, date FROM contacts WHERE name LIKE 'Д%' OR name LIKE 'Е%'"
            self.sorting_filter(self.filt)
        elif self.pushButton_4.hasFocus():
            self.filt = f"SELECT name, phone, date FROM contacts WHERE name LIKE 'Ж%' OR name LIKE 'З%' OR" \
                        f" name LIKE 'И%' OR name LIKE 'Й%'"
            self.sorting_filter(self.filt)
        elif self.pushButton_5.hasFocus():
            self.filt = f"SELECT name, phone, date FROM contacts WHERE name LIKE 'К%' OR name LIKE 'Л%'"
            self.sorting_filter(self.filt)
        elif self.pushButton_6.hasFocus():
            self.filt = f"SELECT name, phone, date FROM contacts WHERE name LIKE 'М%' OR name LIKE 'Н%'"
            self.sorting_filter(self.filt)
        elif self.pushButton_7.hasFocus():
            self.filt = f"SELECT name, phone, date FROM contacts WHERE name LIKE 'О%' OR name LIKE 'П%'"
            self.sorting_filter(self.filt)
        elif self.pushButton_8.hasFocus():
            self.filt = f"SELECT name, phone, date FROM contacts WHERE name LIKE 'Р%' OR name LIKE 'С%'"
            self.sorting_filter(self.filt)
        elif self.pushButton_9.hasFocus():
            self.filt = f"SELECT name, phone, date FROM contacts WHERE name LIKE 'Т%' OR name LIKE 'У%'"
            self.sorting_filter(self.filt)
        elif self.pushButton_10.hasFocus():
            self.filt = f"SELECT name, phone, date FROM contacts WHERE name LIKE 'Ф%' OR name LIKE 'Х%'"
            self.sorting_filter(self.filt)
        elif self.pushButton_11.hasFocus():
            self.filt = f"SELECT name, phone, date FROM contacts WHERE name LIKE 'Ц%' OR name LIKE 'Ч%'" \
                        f"OR name LIKE 'Ш%' OR name LIKE 'Щ%'"
            self.sorting_filter(self.filt)
        elif self.pushButton_12.hasFocus():
            self.filt = f"SELECT name, phone, date FROM contacts WHERE name LIKE 'Ъ%' OR name LIKE 'Ы%'" \
                        f"OR name LIKE 'Ь%' OR name LIKE 'Э%'"
            self.sorting_filter(self.filt)
        elif self.pushButton_13.hasFocus():
            self.filt = f"SELECT name, phone, date FROM contacts WHERE name LIKE 'Ю%' OR name LIKE 'Я%'"
            self.sorting_filter(self.filt)
        elif self.pushButton_14.hasFocus():
            self.filt = "SELECT name, phone, date FROM contacts"
            self.sorting_filter(self.filt)

    def delete_contact(self):
        self.currect_column = self.tableWidget.currentItem().column()
        self.currect_row = self.tableWidget.currentRow()
        if self.currect_column == 0:
            name = self.tableWidget.item(self.currect_row, self.currect_column).text()
            phone = self.tableWidget.item(self.currect_row, self.currect_column + 1).text()
            date = self.tableWidget.item(self.currect_row, self.currect_column + 2).text()
        elif self.currect_column == 1:
            name = self.tableWidget.item(self.currect_row, self.currect_column - 1).text()
            phone = self.tableWidget.item(self.currect_row, self.currect_column).text()
            date = self.tableWidget.item(self.currect_row, self.currect_column + 1).text()
        elif self.currect_column == 2:
            name = self.tableWidget.item(self.currect_row, self.currect_column - 2).text()
            phone = self.tableWidget.item(self.currect_row, self.currect_column - 1).text()
            date = self.tableWidget.item(self.currect_row, self.currect_column).text()
        self.tableWidget.removeRow(self.currect_row)
        database.cur.execute(f"DELETE FROM contacts WHERE name = ? AND phone = ? AND date = ?", (name, phone, date))
        database.conn.commit()

    def edit_contact_2(self):
        if self.count == 0:
            self.count += 1
            if self.currect_column == 0:
                name = self.tableWidget.item(self.currect_row, self.currect_column).text()
                phone = self.tableWidget.item(self.currect_row, self.currect_column + 1).text()
                date = self.tableWidget.item(self.currect_row, self.currect_column + 2).text()
                database.cur.execute(
                    f"UPDATE contacts SET name = '{name}' WHERE phone = '{phone}' and date = '{date}'")
            elif self.currect_column == 1:
                name = self.tableWidget.item(self.currect_row, self.currect_column - 1).text()
                phone = self.tableWidget.item(self.currect_row, self.currect_column).text()
                date = self.tableWidget.item(self.currect_row, self.currect_column + 1).text()
                database.cur.execute(
                    f"UPDATE contacts SET phone = '{phone}' WHERE name = '{name}' and date = '{date}'")
            elif self.currect_column == 2:
                name = self.tableWidget.item(self.currect_row, self.currect_column - 2).text()
                phone = self.tableWidget.item(self.currect_row, self.currect_column - 1).text()
                date = self.tableWidget.item(self.currect_row, self.currect_column).text()
                database.cur.execute(
                    f"UPDATE contacts SET date = '{date}' WHERE name = '{name}' and phone = '{phone}'")
            else:
                pass

            database.conn.commit()
        else:
            pass

    def edit_contact(self):
        self.count = 0
        self.currect_column = self.tableWidget.currentColumn()
        self.currect_row = self.tableWidget.currentRow()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.AllEditTriggers)
        self.tableWidget.setFocus()
        self.push = QtWidgets.QPushButton()
        self.push.clicked.connect(self.immitation_click_mouse)
        self.push.click()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.itemClicked.connect(self.edit_contact_2)
        self.tableWidget.itemChanged.connect(self.edit_contact_2)

    def immitation_click_mouse(self):
        self.tableWidget.editItem(self.tableWidget.item(self.currect_row, self.currect_column))

    def setupUi(self, Form):
        self.birth_names = []
        self.birth_date = []
        self._new = None
        Form.setObjectName("Form")
        Form.resize(700, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(700, 600))
        Form.setMaximumSize(QtCore.QSize(700, 600))
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(510, 50, 171, 241))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(3)
        self.splitter.setObjectName("splitter")
        self.add = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add.setMinimumSize(171, 70)
        self.add.setMaximumSize(171, 70)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.edit = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit.setMinimumSize(171, 70)
        self.edit.setMaximumSize(171, 70)
        self.edit.setFont(font)
        self.edit.setObjectName("edit")
        self.delete_2 = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_2.setMinimumSize(171, 70)
        self.delete_2.setMaximumSize(171, 70)
        self.delete_2.setFont(font)
        self.delete_2.setObjectName("delete_2")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(154, 21, 331, 551))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QtCore.QSize(350, 550))
        self.tableWidget.setMinimumSize(QtCore.QSize(350, 550))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        brush = QtGui.QBrush(QtGui.QColor(206, 206, 206))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(80, 12, 77, 561))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.widget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setHandleWidth(0)
        self.splitter_2.setObjectName("splitter_2")
        self.pushButton = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setToolTipDuration(-1)
        self.pushButton.setStatusTip("")
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setCheckable(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_2.setAcceptDrops(False)
        self.pushButton_2.setToolTipDuration(-1)
        self.pushButton_2.setStatusTip("")
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_3.setAcceptDrops(False)
        self.pushButton_3.setToolTipDuration(-1)
        self.pushButton_3.setStatusTip("")
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_6.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_7.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_8.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_9.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_10.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_11.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_12.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_13.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_14.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout.addWidget(self.splitter_2)
        spacerItem = QtWidgets.QSpacerItem(20, 125, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.update_table()
        self.add.clicked.connect(self.add_contact)
        self.delete_2.clicked.connect(self.delete_contact)
        self.edit.clicked.connect(self.edit_contact)
        self.pushButton.clicked.connect(self.sorting)
        self.pushButton_2.clicked.connect(self.sorting)
        self.pushButton_3.clicked.connect(self.sorting)
        self.pushButton_4.clicked.connect(self.sorting)
        self.pushButton_5.clicked.connect(self.sorting)
        self.pushButton_6.clicked.connect(self.sorting)
        self.pushButton_7.clicked.connect(self.sorting)
        self.pushButton_8.clicked.connect(self.sorting)
        self.pushButton_9.clicked.connect(self.sorting)
        self.pushButton_10.clicked.connect(self.sorting)
        self.pushButton_11.clicked.connect(self.sorting)
        self.pushButton_12.clicked.connect(self.sorting)
        self.pushButton_13.clicked.connect(self.sorting)
        self.pushButton_14.clicked.connect(self.sorting)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add.setText(_translate("Form", "Добавить контакт"))
        self.edit.setText(_translate("Form", "Редактировать"))
        self.delete_2.setText(_translate("Form", "Удалить контакт"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Имя"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Телефон"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Дата рождения"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Form", "АБ"))
        self.pushButton_2.setText(_translate("Form", "ВГ"))
        self.pushButton_3.setText(_translate("Form", "ДЕ"))
        self.pushButton_4.setText(_translate("Form", "ЖЗИЙ"))
        self.pushButton_5.setText(_translate("Form", "КЛ"))
        self.pushButton_6.setText(_translate("Form", "МН"))
        self.pushButton_7.setText(_translate("Form", "ОП"))
        self.pushButton_8.setText(_translate("Form", "РС"))
        self.pushButton_9.setText(_translate("Form", "ТУ"))
        self.pushButton_10.setText(_translate("Form", "ФХ"))
        self.pushButton_11.setText(_translate("Form", "ЦЧШЩ"))
        self.pushButton_12.setText(_translate("Form", "ЪЫЬЭ"))
        self.pushButton_13.setText(_translate("Form", "ЮЯ"))
