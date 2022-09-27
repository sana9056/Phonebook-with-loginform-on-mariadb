from PyQt5 import QtCore, QtGui, QtWidgets
"""
Скрипты для работы с профилем.
Здесь ничего трогать не нужно
#sana9056
"""

class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        self._new = None
        Form.setObjectName("Form")
        Form.resize(400, 200)
        Form.setMinimumSize(QtCore.QSize(400, 200))
        Form.setMaximumSize(QtCore.QSize(400, 200))
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 50, 281, 81))
        self.widget.setObjectName("widget")
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setAcceptDrops(True)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_2.clicked.connect(self.close)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Адрес электронной почты"))
        self.pushButton.setText(_translate("Form", "Сменить пароль"))
        self.pushButton_2.setText(_translate("Form", "Отмена"))
