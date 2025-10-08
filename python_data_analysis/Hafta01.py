# Pyhton ile Veri Analizi Hafta 01
print("Bilişim Sistemleri Mühendisliği Bölümü!")
##
sayi=1

while sayi<10:
    print (sayi)
    sayi+=1 #satir silinirse sonsuz dongu

for sayi in range(1,10):
    print(sayi)

print("Done")

for sayi in range(10,1,-2):
    print(sayi)

for sayi in range(1,10):
    print("sayilar:", sayi+sayi)

başarıNotu =50

if başarıNotu>=65:
    print("Dersi geçmiştir")
else:
    print("Dersin tekrar alınması gerekmektedir")

isim =input("isminizi klavyeden giriniz ")
print(isim)