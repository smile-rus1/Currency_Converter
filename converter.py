# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'конвертер.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(731, 253)
        MainWindow.setFixedWidth(731)
        MainWindow.setFixedHeight(253)
        MainWindow.setStyleSheet("")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 60, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.btn_translate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_translate.setGeometry(QtCore.QRect(70, 160, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_translate.setFont(font)
        self.btn_translate.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn_translate.setStyleSheet("\n"
"\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 18px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"background-color: rgb(130, 130, 130);")
        self.btn_translate.setCheckable(False)
        self.btn_translate.setAutoDefault(False)
        self.btn_translate.setDefault(False)
        self.btn_translate.setFlat(False)
        self.btn_translate.setObjectName("btn_translate")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 90, 331, 61))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.line = QtWidgets.QFrame(self.groupBox_2)
        self.line.setGeometry(QtCore.QRect(229, 0, 21, 61))
        self.line.setStyleSheet("background-color: rgb(129, 129, 129);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.choice_input_currency = QtWidgets.QComboBox(self.groupBox_2)
        self.choice_input_currency.setGeometry(QtCore.QRect(250, 0, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.choice_input_currency.setFont(font)
        self.choice_input_currency.setStyleSheet("")
        self.choice_input_currency.setObjectName("choice_input_currency")
        self.choice_input_currency.addItem("")
        self.choice_input_currency.addItem("")
        self.choice_input_currency.addItem("")
        self.choice_input_currency.addItem("")
        self.form_input = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.form_input.setGeometry(QtCore.QRect(0, 0, 231, 61))
        self.form_input.setStyleSheet(" border-style: outset;\n"
"background-color: rgb(255, 255, 255);\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    font: bold 18px;\n"
"    padding: 6px;")
        self.form_input.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.form_input.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.form_input.setDecimals(2)
        self.form_input.setMaximum(1e+24)
        self.form_input.setObjectName("form_input")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(70, 210, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("\n"
"\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 18px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"background-color: rgb(130, 130, 130);")
        self.btn_exit.setObjectName("btn_exit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 60, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(400, 90, 331, 61))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.line_2 = QtWidgets.QFrame(self.groupBox_3)
        self.line_2.setGeometry(QtCore.QRect(230, 0, 21, 61))
        self.line_2.setStyleSheet("background-color: rgb(129, 129, 129);")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.form_output = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.form_output.setGeometry(QtCore.QRect(0, 0, 231, 61))
        self.form_output.setStyleSheet(" border-style: outset;\n"
"background-color: rgb(255, 255, 255);\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    font: bold 18px;\n"
"    padding: 6px;")
        self.form_output.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.form_output.setReadOnly(True)
        self.form_output.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.form_output.setDecimals(2)
        self.form_output.setMaximum(1e+24)
        self.form_output.setObjectName("form_output")
        self.choice_output_currency = QtWidgets.QComboBox(self.groupBox_3)
        self.choice_output_currency.setGeometry(QtCore.QRect(250, 0, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.choice_output_currency.setFont(font)
        self.choice_output_currency.setStyleSheet("")
        self.choice_output_currency.setObjectName("choice_output_currency")
        self.choice_output_currency.addItem("")
        self.choice_output_currency.addItem("")
        self.choice_output_currency.addItem("")
        self.choice_output_currency.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 90, 71, 61))
        self.label_3.setStyleSheet("\n"
"font: 75 48pt \"Times New Roman\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.lbl_for_date = QtWidgets.QLabel(self.centralwidget)
        self.lbl_for_date.setGeometry(QtCore.QRect(180, 10, 370, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_for_date.setFont(font)
        self.lbl_for_date.setText("")
        self.lbl_for_date.setObjectName("lbl_for_date")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Конвертер валют"))
        self.label_2.setText(_translate("MainWindow", "Сколько получите"))
        self.btn_translate.setText(_translate("MainWindow", "Перевести"))
        self.choice_input_currency.setItemText(0, _translate("MainWindow", "₽"))
        self.choice_input_currency.setItemText(1, _translate("MainWindow", "$"))
        self.choice_input_currency.setItemText(2, _translate("MainWindow", "€"))
        self.choice_input_currency.setItemText(3, _translate("MainWindow", "BYN"))
        self.btn_exit.setText(_translate("MainWindow", "Выход"))
        self.label.setText(_translate("MainWindow", "Сколько хотите поменять"))
        self.choice_output_currency.setItemText(0, _translate("MainWindow", "$"))
        self.choice_output_currency.setItemText(1, _translate("MainWindow", "₽"))
        self.choice_output_currency.setItemText(2, _translate("MainWindow", "€"))
        self.choice_output_currency.setItemText(3, _translate("MainWindow", "BYN"))
        self.label_3.setText(_translate("MainWindow", "→"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())