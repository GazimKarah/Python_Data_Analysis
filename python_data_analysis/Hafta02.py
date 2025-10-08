#Pyton ile Veri Analizi Hafta 02
# değişkenlerin değerleri, spesifik hafızada(memory) farklı adreslerde saklanmaktadır
isim = "Kaya"
şehir = "Kayseri"
plaka = 38
print(id(isim))
print(id(şehir))
print(id(plaka))
print(type(isim))
print(type(şehir))
print(type(plaka))
#  Python programlama dilinde Python tür değiştirici(Python Casting) ile değişken türleri değiştirilebilir
sayı = 5
print(sayı, type(sayı))
print(float(sayı), type(float(sayı)))
print(complex(sayı), type(complex(sayı)))

def ekran_goruntu():
    print("Sakarya university")
    print("Eem")
    print("Sakarya")

ekran_goruntu() #fonksiyon çağırma

def main():
    ekran_goruntu()
    ekran_goruntu()

main()

def toplamaIslemi(x,y):
    toplam=x+y
    ekran='{} ve {} sayılarının toplamı:{}'.format(x,y,toplam)
    print(ekran)

def mainy():
    toplamaIslemi(10, 20) # parametre gönderilmesi
    toplamaIslemi(10000, 20000) # parametre gönderilmesi
    a = int(input("bir sayi giriniz: "))
    b = int(input("yeni bir sayi giriniz: "))
    toplamaIslemi(a, b) # parametre gönderilmesi

mainy()

################### Menü örneği ###################
def print_menu():
    print(35*"-","MENU","-"*35)
    print("1.sayı girişi")
    print("2.toplama")
    print("3.çıkarma")
    print("4.çarpma")
    print("5.bölme")
    print("6.programdan çıkma")
    print(70*"-")

donguDegiskeni=True

sayi1=0
sayi2=0

while donguDegiskeni: #donguDegiskeni false ile değişene kadar devam eder
    print_menu()
    secim=int(input("Seciminizi [1-6] arasinda yapiniz:"))

    if secim==1:
        print("Sayi girisi:")
        sayi1=int(input("Sayi 1:"))
        sayi2 =int(input("Sayi 2:"))

    elif secim!=1 & sayi1==0 & sayi2==0:
        print("Ilk once sayi giriniz:")
        sayi1 = int(input("Sayi 1:"))
        sayi2 = int(input("Sayi 2:"))

    elif secim==2:
        print("Toplama islemi")
        toplamaIslemi(sayi1,sayi2)
    elif secim==3:
        print("Cikarma Islemi")
        cikarma=sayi1-sayi2
        print("Sayilarin cikarilmasi: ",cikarma)
    elif secim==4:
        print("Carpma Islemi")
        carpma=sayi1*sayi2
        print("Sayilarin carpimi: ",carpma)
    elif secim==5:
        print("Bolme Islemi")
        bolme=sayi1/sayi2
        print("Sayilarin Bolmesi: ",bolme)
    elif secim==6:
        print("Programdan Cikis")
        donguDegiskeni=False #döngüden çıkar
    else:
        print("Seciminiz [1-6] arasinda olmali")

################### Menü örneği ###################

def fahrenayt(derece):
 # dereceyi fahrenaytaçevirir
 return(derece * 9 / 5) + 32

for sıcaklık__değer in (20.5, 25.5, 30.2, 35.0):
 print("sıcaklık dönüşümü: ",sıcaklık__değer, ": ",
fahrenayt(sıcaklık__değer))

# Liste Örneği
liste = [i for i in range(10)]
print (liste)
liste = list(range(10))
print (liste)


