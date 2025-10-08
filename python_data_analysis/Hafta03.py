#Python ile Veri Analizi Hafta 03

# Listenin tanımlanması:
sayi = [2, 4, 6, 5, 10, 11]
# sayı listesinin elemanları
print(sayi)

sayılar = [0] * 10
print (sayılar)

#range(stop)
for i in range(3):
    print(i)

print("\n")

#range(start, stop)
for i in range(1, 8):
 print(i)

#liste elemanlarının iterasyonu
sayı = [19, 100, 21, 76, 35, 67 ]
for n in sayı:
    print (n)

liste = [ "Ankara", "İstanbul", "Bursa", "İzmir", "Tekirdağ"]
print(liste)
 # bütün listenin ekranda gösterilmesi
print(liste[0])  # listedeki birinci elemanın(indeks sıfır)ekranda gösterilmesi
print(liste[-1])  # listedeki sonuncu elemanın(indeks -1)ekranda gösterilmesi
print(liste[-3])  # listenin sonundan -3.  elemanın(indeks3) ekranda gösterilmesi

diller = ['Spanish', 'English',  'French', 'German', 'Irish',
'Chinese']
# len listedeki eleman sayısını hesaplar
for indeks in range(len(diller)):
 print('Dil Listesi : ', diller[indeks])

sayı = [19, 100, 21, 76, 35, 67]
indeks = 0
while (indeks < 6):
 print (sayı[indeks])
 indeks+= 1

sicaklik_degerleri = [19, 10, 13, 12, 11, 9, 8]
hafta_ici = sicaklik_degerleri[0:5]
print (sicaklik_degerleri)
print (hafta_ici)

#SLICING – Dilimleme İşlemi
sicaklik_degerleri = [19, 10, 13, 12, 11, 9, 8]
# bütün liste, sondan iki eleman hariç
hafta_ici = sicaklik_degerleri[-7:-2]
print (sicaklik_degerleri)
print (hafta_ici)

#SLICING - Dilimleme
hafta_ici=sicaklik_degerleri[-1]    # listedeki son eleman
print (hafta_ici)
hafta_ici=sicaklik_degerleri[-2:]   # listedeki son iki eleman
print (hafta_ici)
hafta_ici=sicaklik_degerleri[:-2]   # son iki eleman hariç bütün elemanlar
print (hafta_ici)

#SLICING – Dilimleme
hafta_ici=sicaklik_degerleri[::-1]    # Sondan başlayarak bütün elemanlar
print (hafta_ici)
hafta_ici= sicaklik_degerleri[1::-1]   # Sondan başlayarak ilk iki eleman
print (hafta_ici)
hafta_ici= sicaklik_degerleri[:-3:-1]  # Sondan başlayarak son iki eleman
print(hafta_ici)
hafta_ici= sicaklik_degerleri[-3::-1]  # Sondan başlayarak son iki eleman hariç
print (hafta_ici)

#SLICING - Dilimleme
sicaklik_degerleri = [19, 10, 13, 12, 11, 9, 8]
ilk__iki = sicaklik_degerleri[-7:-5] #bütün liste
#sondan 5 eleman hariç
print (sicaklik_degerleri)
print (ilk__iki)

def main():
    # liste oluşturma
    sicaklik = [15.0, 10.5, 13.5, 14.0, 12.5]
    # toplam değişkeni başlangıç değeri
    toplam = 0.0

    # liste elemanlarının toplamı
    for deger in sicaklik:
        toplam += deger

    # ortalama değer hesabı
    ortalama = toplam / len(sicaklik)
    print(ortalama)

# Fonksiyonu çağırmayı unutma!
main()


def veriyerlestirme():
    # Liste
    paket_isimleri = ['AX', 'GP', 'NAV', 'SL', 'CRM']
    # ekran çıktısı
    print('Liste elemanları:')
    print(paket_isimleri)
    # sıfırıncı elemanın yerine veri ilavesi
    paket_isimleri.insert(0, 'SAP')
    # ekran çıktısı
    print('listede veri değiştirme:',paket_isimleri)
    paket_isimleri.insert(4, 'Peoplesoft')
    print('Listeye veri ilave:')
    print(paket_isimleri)

# Fonksiyon çağırma
veriyerlestirme()

def verisilme():
    # Liste
    paket_isimleri = ['AX', 'GP', 'NAV', 'SL', 'CRM']
    # ekran çıktısı
    print('Listedeki veriler:')
    print(paket_isimleri)
    # sıfırıncı elemanın silinmesi.
    paket_isimleri.remove('AX')
    print ('ilk eleman listeden silindi')
    print(paket_isimleri)
    # ekran çıktısı
    print('listedeki son elemanın silinmesi:')
    print(paket_isimleri)
    paket_isimleri.pop()
    print('Listeye veri silme:')
    print(paket_isimleri)

# Fonksiyon çağırma
verisilme()
