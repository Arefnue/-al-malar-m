import sqlite3
import time

class Şarkı():

    def __init__(self,isim,albüm_adı,grup_adı,tür,çıkış_tarihi,süre):

        self.isim = isim
        self.albüm_adı = albüm_adı
        self.grup_adı = grup_adı
        self.tür = tür
        self.çıkış_tarihi = çıkış_tarihi
        self.süre = süre
    def __str__(self):

        return "Şarkının adı: {}\nAlbümün adı: {}\nGrubun adı: {}\nŞarkının türü: {}\nŞarkının çıkış tarihi: {}\nŞarkı süresi: {}\n".format(self.isim,self.albüm_adı,self.grup_adı,self.tür,self.çıkış_tarihi,self.süre)


class Şarkılar():

    def __init__(self):

        self.bağlantı_oluştur()


    def bağlantı_oluştur(self):
        self.baglantı = sqlite3.connect("Müziklerim.db")

        self.cursor = self.baglantı.cursor()

        sorgu = "Create table if not exists müzikler (Şarkının_Adı TEXT,Albümün_Adı TEXT,Grubun_Adı TEXT,Şarkının_Türü TEXT,Çıkış_Yılı TEXT,Şarkı_Süresi REAL)"

        self.cursor.execute(sorgu)
        self.baglantı.commit()

    def baglantı_kes(self):
        self.baglantı.close()

    def şarkıları_göster(self):

        sorgu = "Select * from müzikler"

        self.cursor.execute(sorgu)

        müzikler = self.cursor.fetchall()

        if len(müzikler) == 0:
            print("Hiç şarkınız yok...")
        else:
            for i in müzikler:

                şarkı = Şarkı(i[0],i[1],i[2],i[3],i[4],i[5])
                print(şarkı)

    def şarkı_sorgula(self,isim):

        sorgu = "Select * from müzikler where Şarkının_Adı = ?"

        self.cursor.execute(sorgu,(isim,))

        sorgulanan_müzik = self.cursor.fetchall()

        sorgu2 = "Select * from müzikler"

        self.cursor.execute(sorgu2)

        müzikler = self.cursor.fetchall()

        müzik_isimleri = list()
        for i in müzikler:
            müzik_isimleri.append(i[0])

        if len(müzikler) == 0:
            print("Hiç şarkınız yok...")
        elif not isim in müzik_isimleri:
            print("Böyle bir şarkı bulunamadı...")

        else:
            şarkı = Şarkı(sorgulanan_müzik[0][0],sorgulanan_müzik[0][1],sorgulanan_müzik[0][2],sorgulanan_müzik[0][3],sorgulanan_müzik[0][4],sorgulanan_müzik[0][5])
            print(şarkı)

    def şarkı_ekle(self,şarkı):
        sorgu2 = "Select * from müzikler"
        isim = şarkı.isim
        self.cursor.execute(sorgu2)

        müzikler = self.cursor.fetchall()
        müzik_isimleri = list()
        for i in müzikler:
            müzik_isimleri.append(i[0])
        if isim in müzik_isimleri:
            print("Böyle bir şarkı zaten mevcut...")
        else:
            sorgu = "Insert into müzikler Values(?,?,?,?,?,?)"

            self.cursor.execute(sorgu,(isim,şarkı.albüm_adı,şarkı.grup_adı,şarkı.tür,şarkı.çıkış_tarihi,şarkı.süre))

            self.baglantı.commit()

    def şarkı_sil(self,isim):
        sorgu = "Select * from müzikler where Şarkının_Adı = ?"

        self.cursor.execute(sorgu, (isim,))

        sorgulanan_müzik = self.cursor.fetchall()

        sorgu2 = "Select * from müzikler"

        self.cursor.execute(sorgu2)

        müzikler = self.cursor.fetchall()

        müzik_isimleri = list()
        for i in müzikler:
            müzik_isimleri.append(i[0])

        if len(müzikler) == 0:
            print("Hiç şarkınız yok...")
        elif not isim in müzik_isimleri:
            print("Böyle bir şarkı bulunamadı...")
        else:

            sorgu3 = "Delete from müzikler where Şarkının_Adı = ?"

            self.cursor.execute(sorgu3,(isim,))
            self.baglantı.commit()

    def toplam_şarkı_süresi(self):

        sorgu = "Select * from müzikler"

        self.cursor.execute(sorgu)

        müzikler = self.cursor.fetchall()
        şarkı_süresi = 0
        if len(müzikler) == 0:
            print("Hiç şarkınız yok...")
        else:
            for i in müzikler:

                şarkı_süresi += i[5]
        print("Toplam şarkı süresi:",şarkı_süresi,"dakikadır.")

    def albümün_şarkıları(self,albüm_ismi):

        sorgu = "Select * from müzikler where Albümün_Adı = ?"

        self.cursor.execute(sorgu,(albüm_ismi,))

        albüm_müzikleri = self.cursor.fetchall()

        tüm_şarkıları = []
        if len(albüm_müzikleri) == 0:
            print("Böyle bir albüm yok")
        else:
            for i in albüm_müzikleri:
                tüm_şarkıları.append(i[0])
        for i in tüm_şarkıları:
            print("->",i)







