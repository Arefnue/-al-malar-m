import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3
import time

class kullaniciGirisiPenceresi(QWidget):

    def __init__(self):

        super().__init__()
        #Pencere iskeletini oluşturan fonksiyon
        self.kullanici_girisi_UI()
        #Veritabanını oluşturan ve bağlayan fonksiyon
        self.db_baglan()

    def db_baglan(self):

        #Veritabanı oluşturma ve bağlanma
        self.baglanti = sqlite3.connect("Kullanıcı_Bilgileri.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("Create table if not exists kullanıcı_bilgileri(kullanıcı_adı TEXT,parola TEXT,kilo INT,boy INT,yaş INT,cinsiyet TEXT)")
        self.baglanti.commit()

    def kullanici_girisi_UI(self):

        #Kullanıcı adı girişi
        self.kadi = QLineEdit()
        #Parola girişi ve ayarları
        self.parola = QLineEdit()
        self.parola.setEchoMode(QLineEdit.Password)
        #Giriş yapma butonu ve ayarları
        self.giris_yap_button = QPushButton("Giriş Yap")
        #Yeni kullanıcı oluşturma butonu ve ayarları
        self.yeni_kullanici_button = QPushButton("Kayıt ol")
        #Kullanıcıyı bilgilendirme yazılarının verileceği alan ve ayarları
        self.yazi_alani = QLabel("")
        self.yazi_alani.setAlignment(Qt.AlignCenter)
        self.yazi_alani.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        yazi_alani_font = QFont()
        yazi_alani_font.setPixelSize(20)
        yazi_alani_palette = QPalette()
        yazi_alani_renk = QColor(225,29,29,255)
        yazi_alani_palette.setColor(QPalette.Foreground,yazi_alani_renk)
        self.yazi_alani.setPalette(yazi_alani_palette)
        self.yazi_alani.setFont(yazi_alani_font)

        #Kullanıcı girişi katmanı
        f_layout = QFormLayout()
        f_layout.addRow(QLabel("Kullanıcı Adı:"),self.kadi)
        f_layout.addRow(QLabel("Parola:"),self.parola)

        #Buton katmanı
        h_box = QHBoxLayout()
        h_box.addWidget(self.yeni_kullanici_button)
        h_box.addWidget(self.giris_yap_button)
        #Bilgilendirme alanı ve diğer katmanların birleştirilmesi
        v_box = QVBoxLayout()
        v_box.addLayout(f_layout)
        v_box.addLayout(h_box)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()

        #Pencere özellikleri ve ayarları
        self.setWindowTitle("Kullanıcı Girişi")
        self.setLayout(v_box)
        #Butonların etkinleştirilmesi
        self.yeni_kullanici_button.clicked.connect(self.yeni_kullanici)
        self.giris_yap_button.clicked.connect(self.giris_yap)

        self.show()

    def yeni_kullanici(self):

        #Yeni kullanıcı butonuna tıklanıldığında gerçekleşecek olaylar
        self.close()
        self.kadi.clear()
        self.parola.clear()
        self.yazi_alani.clear()
        yeni_kullanici.show()

    def giris_yap(self):

        #Kullanıcı bilgilerinin alınması ve aktarılması
        kadi = self.kadi.text()
        par = self.parola.text()
        sorgu = "Select * from kullanıcı_bilgileri where kullanıcı_adı = ? and parola = ?"
        self.cursor.execute(sorgu,(kadi,par))
        bilgiler = self.cursor.fetchall()

        #Kullanıcı bilgilerinin onaylanması
        if len(bilgiler) == 0:

            self.yazi_alani.setText("Hatalı giriş!")
            self.parola.clear()

        else:

            #Kullanıcı bilgileri geçerliyse gerçekleşecek olaylar
            self.yazi_alani.setText("Giriş yapılıyor...")
            time.sleep(2)
            uygulama_penceresi.mevcut_degerler_yazi(bilgiler)
            self.close()
            uygulama_penceresi.show()



class yeniKullaniciPenceresi(QWidget):
    #Kayıt oluşturulmak istendiğinde açılacak olan pencere
    def __init__(self):

        super().__init__()
        #Veritabanına bağlayan fonksiyon
        self.baglanti_olustur()
        #Pencere iskeletini oluşturan fonksiyon
        self.yeni_kayit_UI()

    def baglanti_olustur(self):

        #Veritabanına bağlanılır
        self.baglanti = sqlite3.connect("Kullanıcı_Bilgileri.db")
        self.cursor = self.baglanti.cursor()

    def yeni_kayit_UI(self):

        #Yeni kullanıcı adı girişi ve ayarları
        self.kadi = QLineEdit()
        #Yeni parola girişi ve ayarları
        self.parola = QLineEdit()
        self.parola.setEchoMode(QLineEdit.Password)
        #Kullanıcı kilo bilgisi ve ayarları
        self.kilo = QLineEdit()
        #Kullanıcı boy bilgisi ve ayarları
        self.boy = QLineEdit()
        #Kullanıcı yaş bilgisi ve ayarları
        self.yas = QLineEdit()
        #Kullanıcı cinsiyet bilgisi ve ayarları
        self.cinsiyet = QComboBox()
        self.cinsiyet.addItem("Erkek")
        self.cinsiyet.addItem("Kadın")
        #Kayıt olma butonu ve ayarları
        self.kayit_ol_button = QPushButton("Kayıt Ol")
        #Kullanıcı bilgilendirme alanı ve ayarları
        self.yazi_alani = QLabel("")
        
        #Kullanıcı girişi penceresine geri döndüren buton ve ayarları
        self.geri_don_button = QPushButton("Geri dön")

        #Kullanıcı bilgilerinin alındığı katman ve ana katman
        f_layout = QFormLayout()
        f_layout.addRow("Kullanıcı Adı:", self.kadi)
        f_layout.addRow("Parola:", self.parola)
        f_layout.addRow("Kilonuz(kg):", self.kilo)
        f_layout.addRow("Boyunuz(cm):", self.boy)
        f_layout.addRow("Yaşınız:", self.yas)
        f_layout.addRow("Cinsiyetiniz:", self.cinsiyet)
        #Butonların yerleştirildiği katman
        h_box = QHBoxLayout()
        h_box.addWidget(self.geri_don_button)
        h_box.addWidget(self.kayit_ol_button)
        #Katmanların birleştirilmesi ve bilgilendirme alanının eklenmesi
        f_layout.addRow(h_box)
        f_layout.addRow(self.yazi_alani)

        #Pencere özellikleri ve ayarları
        self.setLayout(f_layout)
        self.setWindowTitle("Yeni kayıt")
        #Butonların etkinleştirilmesi
        self.kayit_ol_button.clicked.connect(self.kayit_et)
        self.geri_don_button.clicked.connect(self.geri_don)


    def geri_don(self):

        #Kullanıcı girişi penceresine yönlendiren fonksiyon
        self.close()
        kullanici_girisi.show()
        self.resetle()

    def sayı_mı(self,deger):
        #Sayı yerine farklı bir karakter girildiğinde kullanıcıyı bilgilendiren fonksiyon
        try:

            deger = int(deger)
            return deger

        except ValueError:

            self.kilo.clear()
            self.boy.clear()
            self.yas.clear()
            return "hata"

    def kayit_et(self):

        #Bilgilerin kontrolü için veritabanından bilgilerin alınması
        kadi = self.kadi.text()
        sorgu = "Select * from kullanıcı_bilgileri where kullanıcı_adı = ?"
        self.cursor.execute(sorgu,(kadi,))
        data = self.cursor.fetchall()

        #Bilgilerin kontrolü
        if len(data) != 0:

            self.yazi_alani.setText("Bu kullanıcı adı kullanılmaktadır.")
        else:

            #Kullanıcının girdiği değerlerin kontrolü
            kilo = self.sayı_mı(self.kilo.text())
            boy = self.sayı_mı(self.boy.text())
            yas = self.sayı_mı(self.yas.text())

            #Kullanıcıyı bilgilendirmek için yapılan hata denetleme
            if kilo == "hata" or boy == "hata" or yas == "hata":

                self.yazi_alani.setText("Hatalı değer!")

            else:

                #Yeni bilgilerin vertabanına kaydedilmesi
                sorgu2 = "Insert into kullanıcı_bilgileri Values(?,?,?,?,?,?)"
                self.cursor.execute(sorgu2, (kadi, self.parola.text(), kilo, boy, yas,self.cinsiyet.currentText()))
                self.baglanti.commit()

                #Kullanıcıyı bilgilendirme
                self.yazi_alani.setText("Kaydınız oluşturulmuştur...\nGiriş ekranına yönlendirileceksiniz.")

                #Kullanıcı girişi penceresine yönlendirme
                time.sleep(1)
                self.close()
                self.resetle()
                kullanici_girisi.show()

    def resetle(self):
        #Kullanıcının girmiş olduğu eski değerleri temizler
        self.kadi.clear()
        self.parola.clear()
        self.kilo.clear()
        self.boy.clear()
        self.yas.clear()
        self.yazi_alani.clear()





class uygulamaPenceresi(QWidget):
    #Kullanıcının kişisel verilerine göre şekillendirilmiş ana uygulama penceresi
    def __init__(self):

        super().__init__()
        #Kullanıcı adına göre diğer bilgilerin de yer aldığı liste
        self.bilgiler = list()
        #Pencere iskeletini oluşturan fonksiyon
        self.uygulama()
        #Veritabanına bağlayan fonksiyon
        self.baglanti_olustur()

    def baglanti_olustur(self):
        #Veritabanına bağlanır
        self.baglanti = sqlite3.connect("Kullanıcı_Bilgileri.db")
        self.cursor = self.baglanti.cursor()



    def uygulama(self):

        #Kullanıcının vücüt kitle endeksini gösteren etiket ve ayarları
        self.vki_lbl = QLabel("")
        #Kullanıcının mevcut değerlerini gösteren etiket ve ayarları
        self.mevcut_degerler_lbl= QLabel("")
        #Kullanıcının yeni bilgilerini girebileceği alan ve ayarları
        self.yeni_kilo = QLineEdit()
        self.yeni_boy = QLineEdit()
        self.yeni_yas = QLineEdit()
        #Kullanıcının sağlıklı sayılabileceği en düşük kilo değerini gösteren etiket ve ayarları
        self.hedef_lbl = QLabel("")
        #Yeni girilen verileri gönderen buton ve ayarları
        self.btn = QPushButton("Gönder")
        #Kullanıcıyı bilgilendirme alanı ve ayarları
        self.yazi_alani = QLabel("")
        tanitim_yazisi = QLabel("Diyet Programına Hoşgeldiniz!")

        #Kullanıcı değerlerinin gösterildiği katman
        v_box = QVBoxLayout()
        v_box.addWidget(self.mevcut_degerler_lbl)
        v_box.addStretch()
        v_box.addWidget(self.vki_lbl)
        v_box.addWidget(self.hedef_lbl)
        v_box.addStretch()
        #Kullanıcı bilgilerini güncelleme ve bilgilendirme katmanı
        f_layout = QFormLayout()
        f_layout.addRow(tanitim_yazisi)
        f_layout.addRow("Güncel Kilo Değeri:",self.yeni_kilo)
        f_layout.addRow("Güncel Boy Değeri",self.yeni_boy)
        f_layout.addRow("Güncel Yaş Değeri:",self.yeni_yas)
        f_layout.addRow(self.btn)
        f_layout.addRow(self.yazi_alani)
        #Ana katmanın oluşturulması ve diğer katmanların bağlanması
        main_v_box = QVBoxLayout()
        main_h_box = QHBoxLayout()
        main_h_box.addLayout(f_layout)
        main_h_box.addStretch()
        main_h_box.addLayout(v_box)
        main_h_box.addStretch()
        main_v_box.addLayout(main_h_box)

        #Pencere özellikleri ve ayarları
        self.setLayout(main_v_box)
        self.setGeometry(250,250,500,200)
        #Butonların etkinleştirilmesi
        self.btn.clicked.connect(self.gonder)


    def gonder(self):
        #Güncellenen bilgilerin veritabanına girişi
        sorgu = "Update kullanıcı_bilgileri set kilo = ?,boy = ?, yaş = ?"
        #Karakter kontrolü
        kilo = yeni_kullanici.sayı_mı(self.yeni_kilo.text())
        boy = yeni_kullanici.sayı_mı(self.yeni_boy.text())
        yas = yeni_kullanici.sayı_mı(self.yeni_yas.text())

        #Kullanıcıyı bilgilendiren hata yakalama
        if kilo == "hata" or boy == "hata" or yas == "hata":

            self.yazi_alani.setText("Hatalı değer!")
            self.yeni_yas.clear()
            self.yeni_kilo.clear()
            self.yeni_boy.clear()
        else:

            #Bilgilerin kaydedilmesi
            self.cursor.execute(sorgu,(kilo,boy,yas))
            self.baglanti.commit()
            #Kullanıcının girdiği bilgilerin temizlenmesi
            self.yeni_yas.clear()
            self.yeni_kilo.clear()
            self.yeni_boy.clear()
            #Bilgilendirme mesajı
            self.yazi_alani.setText("Bilgileriniz güncellenmiştir.\nLütfen yeniden başlatınız.")


    def mevcut_degerler_yazi(self,bilgiler):
        #Veritabanından kullanıcıya özgü verilerin alınması ve yazı alanlarında yazılacak yazıların hazırlanması
        for i in bilgiler[0]:

            self.bilgiler.append(i)

        yazi = "Kilonuz: {}\nBoyunuz: {}\nYaşınız: {}".format(
            self.bilgiler[2],
            self.bilgiler[3],
            self.bilgiler[4]
        )
        self.mevcut_degerler_lbl.setText(yazi)

        vki = self.bilgiler[2] / ((self.bilgiler[3]/100)**2)

        self.vki_lbl.setText("Vücüt Kitle Endeksi: {:.2f}".format(vki))

        hedef = 25*((self.bilgiler[3]/100)**2)

        self.hedef_lbl.setText("Hedef Kilo: {:.2f}".format(hedef))



#Döngüyü sağlayan temel uygulama iskeleti
if __name__ == '__main__':

    app = QApplication(sys.argv)

    kullanici_girisi = kullaniciGirisiPenceresi()
    yeni_kullanici = yeniKullaniciPenceresi()
    uygulama_penceresi = uygulamaPenceresi()

    sys.exit(app.exec_())