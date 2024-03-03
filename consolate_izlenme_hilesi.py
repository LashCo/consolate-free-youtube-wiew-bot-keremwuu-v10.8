import sys
import webbrowser
import time
print("consolate'e hoş geldiniz")
print("consolate sayesinde youtube izlenmelerinizi uçurun")
print("NOT: her izlenme 1 concoin'dir")

concoin = input("20 concoin almak için 'x' tuşlayın: ")

if concoin == "x":
    print("Evet, 20 concoin aldınız.")
else:
    print("Program sonlandırıldı.")
    sys.exit()

izlenme_sayisi = int(input("Kaç izlenme istersiniz: "))
URL = input("Videonuzun URL'si: ")

izin = input("UYARI: Şimdi tarayıcınızda " + str(izlenme_sayisi) + " kadar ekran açılacaktır. Sekmeleri kapatmayın ki izlenme artsın! devam etmek için 'y' tuşlayınız: ")
print("programın sağlıklı çalışması için 10 saniye bekleteceğiz...")
if izin == "y":
    time.sleep(10) 
    for _ in range(izlenme_sayisi):
        webbrowser.open(URL)

    print("Program başarılı.")
else:
    print("program sonlandı")
    sys.exit()
