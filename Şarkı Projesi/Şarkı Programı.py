from Şarkı_Özellikler import *


print("""**********************
Şarkı Programı

1.Şarkıları Göster
2.Şarkı Sorgula
3.Şarkı Ekle
4.Şarkı Sil
5.Toplam Şarkı Süresi
6.Albümdeki tüm şarkılar

Çıkmak için 'q' karakterini giriniz.
**********************""")

şarkılar = Şarkılar()

while True:

    işlem = input("İşlem numarasını giriniz:")

    if işlem == "q":
        print("Programdan çıkılıyor...")
        time.sleep(2)
        print("Program sonlandırıldı.")
        break
    elif işlem == "1":
        print("Kontrol ediliyor...")
        time.sleep(2)
        print("*************")
        şarkılar.şarkıları_göster()
        print("*************")

    elif işlem == "2":
        şarkı_ismi = input("Sorgulamak istediğiniz şarkının ismini giriniz:")
        print("Lütfen bekleyiniz...")
        time.sleep(2)
        şarkılar.şarkı_sorgula(şarkı_ismi)

    elif işlem == "3":
        print("Eklemek istediğiniz şarkının özelliklerini giriniz.")
        şarkı_ismi = input("Şarkı ismi:")
        albüm_ismi = input("Albüm ismi:")
        grup_ismi = input("Grup ismi:")
        şarkı_türü = input("Şarkının türü:")
        try:
            çıkış_yılı = int(input("Çıkış yılı:"))
        except ValueError:
            print("Geçersiz yıl!")
            continue
        try:
            şarkının_süresi = float(input("Şarkının süresi(dk.sn):"))
        except ValueError:
            print("Geçersiz süre!")
            continue
        şarkı = Şarkı(şarkı_ismi,albüm_ismi,grup_ismi,şarkı_türü,str(çıkış_yılı),şarkının_süresi)
        print("Kitap kaydediliyor...")
        time.sleep(2)
        şarkılar.şarkı_ekle(şarkı)

    elif işlem == "4":
        isim = input("Silmek istediğiniz şarkının ismini giriniz:")
        print("İşlem gerçekleştiriliyor...")
        time.sleep(2)
        şarkılar.şarkı_sil(isim)

    elif işlem == "5":

        şarkılar.toplam_şarkı_süresi()

    elif işlem == "6":
        albüm = input("Şarkılarını görmek istediğiniz albümün ismini giriniz:")
        print("Kontrol ediliyor...")
        time.sleep(2)
        şarkılar.albümün_şarkıları(albüm)
    else:
        print("Hatalı işlem!")
