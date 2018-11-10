import requests
import sys
from PyQt5.QtWidgets import QWidget,QAction,QApplication,QLabel,QLineEdit,QMainWindow,QVBoxLayout,QHBoxLayout,QPushButton,QComboBox,qApp

from bs4 import BeautifulSoup

class Arayuz(QWidget):

    def __init__(self):

        super().__init__()
        self.birim_fiyatı = self.baglanti_olustur()[0]

        self.init_ui()

    def baglanti_olustur(self):

        url = "https://www.doviz.com"

        response = requests.get(url)

        html_icerigi = response.content

        soup = BeautifulSoup(html_icerigi,"html.parser")
        birimler = list()

        USD = soup.find("li",{"data-table-homepage-key":"USD"}).text
        USD = USD.strip()
        USD = USD.replace(",",".")
        USD = USD[32:36]
        USD = float(USD)
        birimler.append(USD)

        EURO = soup.find("li",{"data-table-homepage-key":"EUR"}).text
        EURO = EURO.strip()
        EURO = EURO.replace(",", ".")
        EURO = EURO[32:36]
        EURO = float(EURO)

        birimler.append(EURO)

        altin = soup.find("li",{"data-table-homepage-key": "ceyrek-altin"}).text
        altin = altin.strip()
        altin = altin.replace(",",".")
        altin = altin[8:14]
        altin = float(altin)

        birimler.append(altin)

        return birimler


    def init_ui(self):
        self.baglanti_olustur()
        self.miktar_etiket = QLabel("Çevirmek istediğiniz miktarı giriniz:")
        self.miktar_alani = QLineEdit("1")


        self.cevirilicek_birim = QComboBox()
        self.cevirilicek_birim.addItem("Dolar")
        self.cevirilicek_birim.addItem("Euro")
        self.cevirilicek_birim.addItem("Çeyrek Altın")
        self.cevirilicek_birim.currentIndexChanged.connect(self.birim_belirle)

        self.cevir = QPushButton("Çevir")

        self.yazi_alani = QLabel("")

        h_box = QHBoxLayout()

        v_box = QVBoxLayout()
        h_box.addStretch()
        v_box.addStretch()
        v_box.addWidget(self.miktar_etiket)
        v_box.addWidget(self.miktar_alani)
        v_box.addWidget(self.cevirilicek_birim)

        h_box.addWidget(self.cevir)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Döviz Programı")
        self.setGeometry(200,200,100,100)
        self.setLayout(h_box)


        self.cevir.pressed.connect(self.doviz_cevir)



    def birim_belirle(self):

        liste = self.baglanti_olustur()


        if self.cevirilicek_birim.currentText() == "Dolar":
            self.birim_fiyatı = (liste[0])
        elif self.cevirilicek_birim.currentText() == "Euro":
            self.birim_fiyatı = (liste[1])
        elif self.cevirilicek_birim.currentText() == "Çeyrek Altın":
            self.birim_fiyatı = (liste[2])


    def doviz_cevir(self):
        self.baglanti_olustur()


        try:
            birim = self.miktar_alani.text()
            birim = int(birim)
            self.yazi_alani.setText("{} TRY".format(self.birim_fiyatı * birim))

        except:
            self.yazi_alani.setText("Hatalı Değer!")


class Menuler(QMainWindow):

    def __init__(self):
        super().__init__()

        self.arayuz = Arayuz()

        self.setCentralWidget(self.arayuz)

        self.menuleri_olustur()

    def menuleri_olustur(self):

        menubar = self.menuBar()

        dosya =  menubar.addMenu("Dosya")


        cikis_yap = QAction("Çıkış",self)
        cikis_yap.setShortcut("Ctrl+Q")


        dosya.addAction(cikis_yap)

        dosya.triggered.connect(self.response)
        self.setWindowTitle("Döviz İşlemleri Programı")


    def response(self,action):

        if action.text() == "Çıkış":
            qApp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    menu = Menuler()
    menu.show()
    sys.exit(app.exec_())