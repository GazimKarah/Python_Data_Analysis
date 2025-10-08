#Python ile Veri Analizi Hafta 05

#pandas, veri analizi işlemlerini hızlı ve kolay hale getirmek için tasarlanmıştır.
#pandasveri yapıları olarak, Series ve DataFrame’i kapsamaktadır.
#pandas, döngüsüz veri işleme yapabilir.
#pandas kütüphanesinin NumPykütüphanesinden farkı:
# 1- pandastablolar ve farklı türde verilerle çalışır.  NumPykütüphanesi ise, homojen sayısal dizi(array)
# verileri ile çalışmak için uygun bir kütüphanedir.

#Pandas kütüphanesindeki Seri veri yapısı, herhangi bir veri türünü depolayabilen tek boyutlu dizilerdir.

import pandas as pd
import numpy as np
import sys
import matplotlib as plt
import matplotlib.pyplot as plt
# Bu ise doğrudan grafik fonksiyonlarını içerir: plt.plot(), plt.hist(), plt.show() ...


print(sys.version)
print("pandas kütüphanesi versiyon: ", pd.__version__)
pd.show_versions() #yüklenmiş kütüphaneler

#seri_ismi = pd.Series([data], name=[indeks ismi])
sayılar = pd.Series([0, 1, 4, 9, 16, 25, 36, 49], name='Sayı Kareleri')
print (sayılar)

#indeks oluşturulması
#'Kuzey Denizi', 'Atlas', 'Hint', 'Pasifik', 'Güney'

okyanus_derinlik = pd.Series([1205, 3646, 3741, 4080,
3270], index=['Kuzey Denizi',  'Atlas', 'Hint', 'Pasifik',
'Güney Okyanusu'])
print (okyanus_derinlik)
#Görüldüğü üzere index fonksiyonu ile indeksleme yapılıyor, yukarıdaki diğer örnekte name kullanıldı

#indeks ve dilimleme işlemleri (Indexing and Slicing)
print (okyanus_derinlik)
print ("\n")

#print (okyanus_derinlik[2])
#FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version,
# integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]

print(okyanus_derinlik.iloc[2]) #Yukarıdaki çağırma yöntemi
# kullanım dışı bırakılmış durumda ve gelecekte ve şuan bu yöntem ile çağrılma
# yapılacak
print ("\n")
print (okyanus_derinlik[0:3]) #dilimleme işlemi
print ("\n")
print (okyanus_derinlik['Pasifik'])
print("\n")
print (okyanus_derinlik['Atlas':'Pasifik'])#dilimleme işlemi
print("\n")

#Dictionary ile Series Deklarasyonu (tanımlaması)
okyanus_derinlik = pd.Series({
 'Kuzey Denizi': 1205,
 'Atlas': 3646,
 'Hint': 3741,
 'Pasifik': 4080,
 'Güney Okyanusu': 3270
}) #dictionary, çünkü neden; süslü parantez key:value
print (okyanus_derinlik)

max_derinlik = pd.Series({
 'Kuzey Denizi': 5567,
 'Atlas': 8486,
 'Hint': 7906,
 'Pasifik': 10803,
 'Güney Okyanusu': 7075
})
print(max_derinlik)

print("\n")

derinlikler= pd.DataFrame({
    "ortalama Derinlik(metre)":okyanus_derinlik,
    "maksimum Derinlik(metre)":max_derinlik

})
print(derinlikler)
print("\n")

#yeni dataFrame tanımlanması
df=derinlikler

print(df)
print("\n")

print(df.head(2)) #ilk 2 veri
print("\n")

print(df.head(0))
print("\n")

print(df.head(1))
print("\n")

print(df.tail(2)) #son 2 veri
print("\n")

print(df.sample())

#günlük tarih oluşturma
print("\n")
dates = pd.date_range('20170101', periods=14)
print(dates)
print("\n")

dates=pd.date_range("20170101",periods=14,freq="ME") #aylar için
print(dates)
print("\n")

print(pd.date_range ( start = '1/1/2018', end = '1/08/2018' ))
print("\n")

dates = pd.date_range( '20170101', periods= 14 , freq= '2D')

#DataFrame:
#Veritabanı Yönetim Sistemlerinde kullanılan,
#veritabanı yapısındaki tabloya benzemektedir.
#Dikdörtgen grid’lerden meydana gelmiştir.
#Her bir satırda bir instance, record veya kayıt vardır.
#Her sütun ise, belirli bir değişken için veri içeren bir
#vektördür.
#Python pandas kütüphanesinde bulunan DataFrame,
#R Programlama dilindeki DataFrame’in benzeridir.

print("\n")

data_Seti=pd.read_csv("https://raw.githubusercontent.com/pcsanwald/kaggle-titanic/refs/heads/master/train.csv") #link raw olmalı ve tırnak içinde olmalı
#üstteki kod pandas kullanılarak veri setinin dataframe’e alınması
print(data_Seti)
#describe() fonksiyonu ile veri setindeki nümerik alanlar incelenebilir,
print("\n")
print (data_Seti.describe().T)
#bu durumda veri seti büyük olduğundan tüm satırlar ve sütunlar gözükmeyebilir
#pd.reset_option('display.max_columns')
#pd.reset_option('display.max_rows')
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
#bu kodlar ile tüm satılar sütunlar gözükme açılabilir lakin veri seti büyüdüğünde
#Terminali boğacağı için tavsiye edilmez ve sonrak iki kodda bu ayarı sıfırlar
#Ayrıca describe komutu sadece nümerik incelediğinden nümerik olmayan değerler
#Gözükmez bundan kaynaklı gözükmesini istiyorsak aşağıdaki komutu kullanırız
print("\n")
print(data_Seti.describe(include='all').T)

# Nümerik olmayan alanların frekans dağılımı açısından analizi:
print (data_Seti['name'].value_counts())
print("\n")
#Histogram diyagramı:
data_Seti['survived'].hist(bins=50)
plt.show()
data_Seti['survived'].value_counts().plot(kind="bar")
plt.show()