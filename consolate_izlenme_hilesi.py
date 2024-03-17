#gerekli kütüphaneleri ekledim
import sys
import webbrowser
import time
#bilgi
print("consolate'e hoş geldiniz")
print("consolate sayesinde youtube izlenmelerinizi uçurun")
print("NOT: her izlenme 1 concoin'dir")
#concoin almak için x tuşlıyacak
concoin = input("20 concoin almak için 'x' tuşlayın: ")

if concoin == "x":
    print("Evet, 20 concoin aldınız.")
else:
    print("Program sonlandırıldı.")
    sys.exit()#eğer x derse 20 concoin alıcak demesse program sonlanıcak
#genal sorular
izlenme_sayisi = int(input("Kaç izlenme istersiniz: "))
URL = input("Videonuzun URL'si: ")
#uyarı
izin = input("UYARI: Şimdi tarayıcınızda " + str(izlenme_sayisi) + " kadar ekran açılacaktır. Sekmeleri kapatmayın ki izlenme artsın! devam etmek için 'y' tuşlayınız: ")
print("programın sağlıklı çalışması için 10 saniye bekleteceğiz...")
if izin == "y":
    time.sleep(10) #10 saniye bekliyecek
    for _ in range(izlenme_sayisi):#ne kadar izlenme istediyse URL değişkenini kullanarak videosunu arka planda açıcak
        webbrowser.open(URL)

    print("Program başarılı.")
else:
    print("program sonlandı")
    sys.exit()
