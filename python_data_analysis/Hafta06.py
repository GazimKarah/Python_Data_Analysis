#Python ile Veri Analizi Hafta 06

#NumPy kütühanesi python programlama dilinde, bilimsel hesaplama için
#kullanılan bir kütüphanedir.

#pandas, PYTHON Programlama Dili için geliştirilen açık kaynak kodlu bir
# veri analizi kütüphanesidir. Veri yapıları: Series (object), DataFame (object), Panel
#DataFrame‘in indeks, sütunlarve veriler (değerler) olmak üzere 3 bileşeni vardır

import numpy as np
import pandas as pd
import math as m
import os


#Bu araçlararasında, ilişkisel veritabanları (MS SQL Server, Oracle), elektronik
# tablolar (Excel), olay(event) işleme sistemleri (Apache Spark gibi) ve R Programlama
# Dili ve pandas kütüphanesi gibi araçlar bulunmaktadır.

#pandas öncelikle, read_csv fonksiyonunu kullanarak diskten belleğe(memory) ve
# DataFrame'e veri okur.İndeks etiketi ve sütun adı, sırasıyla indeksin ve
# sütunların tek tek üyelerini ifade eder. İndeks terimi, tüm indeks etiketlerini,
# sütun terimi ise tüm sütun adlarını gösterir.

#--------------------------------O-------------------------------------------

# DataFrame yapısının Series’den, Series’in de liste(list) nesnesi ile oluşturulması:

ürün = ["PC Bilgisayar", "Yazıcı", "Tablet", "Laptop", "Mouse"]
print(type(ürün))
ürün_seri = pd.Series(ürün)
print(type(ürün_seri))
print("\n")

marka=["X","Y","Z","K","L"]
marka_Seri = pd.Series(marka)
fiyat = [10700, 3000, 5000, 18000, 20]
fiyat_seri = pd.Series(fiyat)

df_ürün = pd.DataFrame(ürün_seri)
print(df_ürün)
print("\n")

df_ürün = df_ürün.rename(columns={0:"Ürün"}) #burada indeks satırından sonra başlayan 0. sütünun adını değişiyoruz
print(df_ürün)
print("\n")

df_marka = pd.DataFrame(marka_Seri)
print(df_marka)
print("\n")

df_marka = df_marka.rename(columns = {0:'Marka'})
print(df_marka)
print("\n")

df_fiyat = pd.DataFrame(fiyat_seri)
print(df_fiyat)
print("\n")

df_fiyat = df_fiyat.rename(columns = {0:'Fiyat'})
print(df_fiyat)
print("\n")

df_malzeme = pd.concat([df_ürün, df_marka, df_fiyat ], axis=1)
print(df_malzeme)
print("\n")
print(type(df_malzeme))
# concat fonksiyonu bir ekseni dikkate alarak dataFrame’leri birleştirir.
# axis=1 sütunları göstermektedir, axis= 0 satırları gösterir

#--------------------------------O-------------------------------------------

#Geçmiş 3 yıl TTKOM Verilerini inceleme

#import pandas as pd
#import numpy as np

#csv dosyasından veri yüklenmesi (CSV = Comma-Separated Values)

veri= pd.read_csv("C:\\Users\\gazi\\Desktop\\GAZI_MUHAMMED_KALKAN_DERS_ICERICKLERI\\Phyton ile Veri Analizi\\TTKOM_gecmis_verileri_3_yillik.csv",sep=",",quotechar='"',encoding="utf-8-sig")
# sep="," → Veride sütunlar virgül ile ayrıldığı için, bu parametre sütunları doğru bölmemizi sağlar.
# quotechar='"' → Tüm hücre değerleri çift tırnak içinde yazıldığı için,
# bu parametreyle Pandas tırnak içindeki virgüllerin ayraç olmadığını anlar,
# yani tırnak içindeki virgülleri bölmeden aynı hücrede bırakır.
# encoding="utf-8-sig" → Bu veri dosyasının başında gizli bir BOM (Byte Order Mark) karakteri vardı.
# Bu karakter, özellikle Excel gibi programlarda kaydedilen CSV dosyalarının başına eklenebilir.
# Eğer sadece encoding="utf-8" kullanılırsa, Pandas bu gizli karakteri tanıyamaz
# ve bu da ilk sütun adının bozulmasına ("﻿Tarih" gibi görünmesine) neden olur.
# utf-8-sig ise bu BOM karakterini otomatik olarak tanır ve düzgün şekilde yok sayar.

#with open("C:\\Users\\gazi\\Desktop\\GAZI_MUHAMMED_KALKAN_DERS_ICERICKLERI\\Phyton ile Veri Analizi\\TTKOM_gecmis_verileri_3_yillik.csv", encoding="utf-8") as f:
#    print(f.readline())


#veri seti başlangıcından 2 adet veri okuma

print("\n")
print(veri.head(2))
print("\n")

# Klasördeki dosyalar os.listdir() methodu ile listelenir
for sayaç in os.listdir("C:\\Users\\gazi\\Desktop\\GAZI_MUHAMMED_KALKAN_DERS_ICERICKLERI\\Phyton ile Veri Analizi\\"):
    print(sayaç)
print("\n")
#veri setinin listelenmesi
print(veri.to_string())
print("\n")

print(veri.columns)
#Eğer düz print(veri) yapılırsa veri sayısı 60 adedi aşarsa ilk ve son 5 veri listelenir

#read.csv() fonksiyonu ile, csv uzantılı dosyalardaki verilerden bir DataFrame oluşturur.
#DataFrame’deki bir sütun, bir Seri olarak seçilebilir.
#Bu şekilde indeks ve veri listelenebilir.

#sütun veri türleri
print(veri.dtypes)
print("\n")

# dataset inceleme
print(veri.info())
print("\n")

print(type(veri))
print("\n")

# toplam veri sayısı
print('Toplam Veri Sayısı = ', veri.size)
print('Boyut = ', veri.ndim) # boyut sayısı
print('Satır ve Sütun Sayıları = ', veri.shape)
print("\n")

print(veri.columns.tolist())
print("\n")
print(veri.columns)
print(veri.head())

print("\n")

#print(veri["Tarih"])

# bütün name space import edilebilir from math import

print(m.factorial(5))
print("\n")

# isin() metodu kullanımı

data = {
 "isim": ["Meltem", "Sema", "Kaya"],
 "yaş": [30, 40, 50],
 "Şehir": ["Erzurum", "Uşak", "Kayseri"],
}
print("\n")

print(data)
print("\n")

df = pd.DataFrame(data)
print(df)
print("\n")

print(df.isin([50, 40]))

#Bütün DataFrame'i kontrol eder eğer verilen 40 50 varsa true döndürürür yoksa false