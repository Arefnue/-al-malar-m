import sys
import sqlite3
from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):


    def __init__(self):

        super().__init__()
        self.baglanti_olustur()
        self.init_ui()
    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("Kullanıcı_Bilgileri.db")
        self.cursor = self.baglanti.cursor()

        self.cursor.execute("Create Table If not exists üyeler(kullanıcı_adı TEXT,parola TEXT)")

        self.baglanti.commit()

    def init_ui(self):

        self.kullanici_adi = QtWidgets.QLineEdit()
        self.kullanici_adi_etiket = QtWidgets.QLabel("Kullanıcı Adı:")
        self.parola = QtWidgets.QLineEdit()
        self.parola_etiket = QtWidgets.QLabel("Parola:")
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giriş = QtWidgets.QPushButton("Giriş Yap")
        self.kayit = QtWidgets.QPushButton("Kayıt Ol")
        self.yazi_alani = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi_etiket)
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola_etiket)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.giriş)
        v_box.addWidget(self.kayit)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()

        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Kullanıcı Girişi")
        self.giriş.clicked.connect(self.login)
        self.kayit.clicked.connect(self.register)


        self.show()
    def login(self):

        adi = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("Select * from üyeler where kullanıcı_adı = ? and parola = ?",(adi,par))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.yazi_alani.setText("Böyle bir kullanıcı yok\nLütfen tekrar deneyin.")
        else:
            self.yazi_alani.setText("Hoşgeldiniz " + adi)

    def register(self):
        adi = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("Select * from üyeler where kullanıcı_adı = ? ",(adi,))

        data = self.cursor.fetchall()
        if not len(data) == 0:
            self.yazi_alani.setText("Bu kullanıcı adı kullanılmaktadır.\nLütfen farklı bir kullanıcı adı giriniz.")
        else:
            sorgu = "Insert into üyeler Values(?,?)"
            self.cursor.execute(sorgu,(adi,par))
            self.baglanti.commit()




app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())