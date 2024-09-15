import random

print("Sayı Tahmin Oyununa Hoş Geldiniz!")
a = random.randint(1, 100)
print("1-100 arası bir sayı tutuldu.")
hak_sayisi = 5  

while True: 
    if hak_sayisi == 0:
        print("Maalesef, tahmin hakkınız kalmadı. Doğru sayı:", a)
        break
    
    print(f"Kalan hak sayınız: {hak_sayisi}")
    b = int(input("Tahmininizi giriniz: "))

    if b > 100 or b < 1:
        print("Hatalı giriş! Lütfen 1-100 arası bir sayı giriniz.")
    elif a > b:
        print("Daha büyük bir sayı tahmin edin.")
      
    elif a < b:
        print("Daha küçük bir sayı tahmin edin.")
        
    else:
        print("Tebrikler, doğru bildiniz!")
        break

    hak_sayisi = hak_sayisi - 1 
