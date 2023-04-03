import random         #Random kütüphanesini dahil ettik
import time           #Zaman kütüp dahil ettik

print(""" ***********************

Sayı Tahmin Oyunu

1 ile 40 arasında sayılar
 
********************

""")

rastgele_sayı = random.randint(1,40)
tahmin_hakkı = 7

while True :
    sayı = int(input("Lütfen bir sayı giriniz : "))

    if (rastgele_sayı == sayı ) :
        print("Tahmin Sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler Doğru Tahmin...")
        break

    elif (rastgele_sayı < sayı) :
        print("Tahmin Sorgulanıyor...")
        time.sleep(1)
        print("Daha küçük bir sayı giriniz")
        tahmin_hakkı -= 1
        print("Kalan tahmin hakkınız: ",tahmin_hakkı)

    elif (rastgele_sayı > sayı) :
        print("Tahmin Sorgulanıyor...")
        time.sleep(1)
        print("Daha büyük bir sayı giriniz. ")
        tahmin_hakkı -= 1
        print("Kalan tahmin hakkınız: ", tahmin_hakkı)

    if (tahmin_hakkı == 0) :
        print("Tahmin hakkınız doldu...")
        print("Sayımız : ",rastgele_sayı)
        break