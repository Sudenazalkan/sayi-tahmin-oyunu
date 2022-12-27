import random

x = random.randint(1,100)
print("Sayı tahmin oyununa hoşgeldiniz :)")
hak = int(input("Hak sayısını giriniz:"))
soru_puan = 100/hak
toplam = 100
i=0
while i<hak:
    i+=1
    tahmin=int(input("Tahmininizi yazınız:"))
    if tahmin==x:
        print("Tebrikler doğru tahmin")
        print("Puanınız:{}".format(toplam))
        break
    if tahmin<x:
        print("Yukarı")
        toplam=toplam-soru_puan
        print("Puanınız:{}".format(toplam))
    if tahmin>x:
        print("Aşağı")
        toplam=toplam-soru_puan
        print("Puanınız:{}".format(toplam))
    if i==hak:
        print("Hakkınız bitti")

