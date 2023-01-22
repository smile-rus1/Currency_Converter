from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from converter import Ui_MainWindow
from bs4 import BeautifulSoup

import sys
import re
import requests


class Main(QtWidgets.QMainWindow):
    urls = {
        "url_main": "https://myfin.by/converter/rub-byn",

        "url_rus_for_bel": "https://myfin.by/converter/rub-byn/1",
        "url_rus_for_usd": "https://myfin.by/converter/rub-usd/1",
        "url_rus_for_eur": "https://myfin.by/converter/rub-eur/1",

        "url_bel_for_rus": "https://myfin.by/converter/byn-rub/1",
        "url_bel_for_usd": "https://myfin.by/converter/byn-usd/1",
        "url_bel_for_eur": "https://myfin.by/converter/byn-eur/1",

        "url_usd_for_eur": "https://myfin.by/converter/usd-eur/1",
        "url_usd_for_rub": "https://myfin.by/converter/usd-rub/1",
        "url_usd_for_bel": "https://myfin.by/converter/usd-byn/1",

        "url_eur_for_usd": "https://myfin.by/converter/eur-usd/1",
        "url_eur_for_rus": "https://myfin.by/converter/eur-rub/1",
        "url_eur_for_bel": "https://myfin.by/converter/eur-byn/1",
    }
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_exit.clicked.connect(lambda: self.exit())
        self.ui.btn_translate.clicked.connect(lambda: self.show_currency())

        self.show_date()

    def error(self):
        mes = QMessageBox()
        mes.setIcon(QMessageBox.Warning)
        mes.setWindowTitle("ERROR")
        mes.setStandardButtons(QMessageBox.Ok)
        mes.setText("Ошибка, не правильные данные")
        mes.exec_()

    def exit(self):
        mb = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if mb == QMessageBox.Yes:
            sys.exit(1)

    def parsing(self):
        url = ""
        currency_input = self.ui.choice_input_currency.currentText()
        currency_output = self.ui.choice_output_currency.currentText()

        """ можно потом оптимизировать сделать словарь в словаре и пробегаясь по словарю доставать значения """
        if currency_input != currency_output:
            if currency_input == "₽":
                if currency_output == "BYN":
                    url = self.urls["url_rus_for_bel"]
                elif currency_output == "$":
                    url = self.urls["url_rus_for_usd"]
                elif currency_output == "€":
                    url = self.urls["url_rus_for_eur"]

            elif currency_input == "BYN":
                if currency_output == "₽":
                    url = self.urls["url_bel_for_rus"]
                elif currency_output == "$":
                    url = self.urls["url_bel_for_usd"]
                elif currency_output == "€":
                    url = self.urls["url_bel_for_eur"]

            elif currency_input == "€":
                if currency_output == "₽":
                    url = self.urls["url_eur_for_rub"]
                elif currency_output == "$":
                    url = self.urls["url_eur_for_usd"]
                elif currency_output == "BYN":
                    url = self.urls["url_eur_for_byn"]

            elif currency_input == "$":
                if currency_output == "₽":
                    url = self.urls["url_usd_for_rub"]
                elif currency_output == "€":
                    url = self.urls["url_usd_for_eur"]
                elif currency_output == "BYN":
                    url = self.urls["url_usd_for_bel"]

        res = requests.get(url, headers=self.header)
        soup = BeautifulSoup(res.content, "html.parser")
        currency = soup.find("span", class_="converter-100__info-currency-bold")
        self.summ = re.findall(r"\d.....", currency.text)
        date_data = soup.find("div", class_="converter-100__short_text")
        reg = re.findall(r"по курсу Нацбанка на \d+ .+", date_data.text)

        # print(reg[0].capitalize())
        # print(eval(self.summ[0]))

    def show_date(self):
        url = "https://myfin.by/converter/rub-byn/1"
        res = requests.get(url)
        soup = BeautifulSoup(res.content, "html.parser")
        date_data = soup.find("div", class_="converter-100__short_text")
        reg = re.findall(r"по курсу Нацбанка на \d+ .+", date_data.text)
        self.ui.lbl_for_date.setText(reg[0].capitalize().center(10," "))


    def show_currency(self):
        try:
            self.parsing()
            amount = eval(self.ui.form_input.text())
            total = amount[0] * eval(self.summ[0])
            self.ui.form_output.setValue(total)

        except:
            self.error()


def main():
    app = QtWidgets.QApplication([])
    application = Main()
    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
