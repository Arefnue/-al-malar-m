import requests
import sys
from PyQt5.QtWidgets import QWidget,QAction,QApplication,QLabel,QLineEdit,QMainWindow,QVBoxLayout,QHBoxLayout,QPushButton,QComboBox,qApp,QScrollBar,QScrollArea,QListWidget,QListWidgetItem
import os
from bs4 import BeautifulSoup
from random import randint
from time import sleep


class Arayuz(QWidget):

    def __init__(self):
        super().__init__()

        self.veriler = self.verileri_al()

        self.initUI()


    def verileri_al(self):

        url = "https://www.imdb.com/chart/top"

        response = requests.get(url)

        html_icerigi = response.content

        soup = BeautifulSoup(html_icerigi,"html.parser")

        filmler = soup.find_all("td",{"class":"titleColumn"})
        ratingler = soup.find_all("td",{"class":"ratingColumn imdbRating"})

        liste = list()

        for i,j in zip(filmler,ratingler):
            i = i.text
            j = j.text

            i = i.strip()
            j = j.strip()

            i = i.replace("\n","")
            j = j.replace("\n","")

            i = i.replace("("," (")


            liste.append((i,j))


        return liste



    def initUI(self):

        self.rastgele = QPushButton("Rastgele Seçim")

        self.yazi_alani = QLabel(self.yazı_yap())
        self.yazi_alani2 = QLabel("")
        self.talimat = QLabel("IMDB Programına Hoşgeldiniz!")




        v_box = QVBoxLayout()
        h_box = QHBoxLayout()

        v_box.addStretch()
        v_box.addWidget(self.talimat)
        v_box.addSpacing(25)


        h_box.addWidget(self.rastgele)

        v_box.addLayout(h_box)
        v_box.addWidget(self.yazi_alani2)
        v_box.addStretch()




        v_box2 = QVBoxLayout()
        h_box2 = QHBoxLayout()
        h_box2.addSpacing(50)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.yazi_alani)

        h_box2.addWidget(scroll_area)


        h_box2.addStretch()

        v_box2.addSpacing(25)
        v_box2.addLayout(h_box2)

        v_main = QVBoxLayout()
        h_main = QHBoxLayout()
        h_main.addLayout(v_main)
        h_main.addLayout(v_box)
        h_main.addLayout(v_box2)

        self.setLayout(h_main)

        self.setFixedSize(700,600)
        self.setWindowTitle("IMDB Top 250 Seçim Programı")


        self.rastgele.pressed.connect(self.random_film)




    def yazı_yap(self):
        veriler = self.veriler
        yazi = ""
        for i in veriler:
            yazi = yazi +i[0] + " : " +i[1]+"\n"

        return yazi

    def random_film(self):
        veriler = self.veriler
        yazi = ""
        rastgele_sayı = randint(1,250)

        yazi = yazi + veriler[rastgele_sayı-1][0]+" : "+veriler[rastgele_sayı-1][1]
        self.yazi_alani2.setText(yazi)






if __name__ == '__main__':
    app = QApplication(sys.argv)

    arayuz = Arayuz()
    arayuz.show()
    sys.exit(app.exec_())
