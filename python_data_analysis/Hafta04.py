#Python ile Veri Analizi Hafta 04

Tuple001=(100) #Tuple veri yapısı, Parantez içinde gösterilir

print(Tuple001)

Tuple002 = (100, 200, 300, 350)
#Şimdi indeks ve dilimleme işlemleri gösterilecektir

print(Tuple002[0:2])
print(Tuple002[-1])
print(Tuple002[2])

# tuple’a yeni eleman ilave edilmesi
Tuple003 = (100, 200, 300, 400)
print(Tuple003)
yeniTuple = Tuple003
yeniTuple += (500,)
Tuple003 += (5000,)
print(yeniTuple)
print(Tuple003,"\n")

#Tuple Sıralama(Ascending Order Sorting- Küçükten büyüğe sıralama)
sicaklik_degeri = (10, 13, 14, 9, 8, 16, 11)
print (sicaklik_degeri, "\n")
sicaklik_degeri = sorted(sicaklik_degeri)
print(sicaklik_degeri)

#Tuple Büyükten Küçüğe Sıralama (Descending Order-- Sorting)
sicaklik_degeri = sorted(sicaklik_degeri, reverse = True)
print(sicaklik_degeri)

liste=[10, 30, 50]
tuple=(60, 65, 70)
print (liste)
print (tuple)
#veri elemanı değişikliği
liste[1]=100
#tuple[1]=300 #TypeError: 'tuple' object does not support item assignment
#tuple veri tipi bu tarz bir eleman değişikliğine uygun değildir.

#tuple[1] elemanın değerinin 300 olarak değiştirilmesi
n=1
tuple= tuple[ : n] + (300 ,) + tuple[n + 1 : ] #tuple = (60,) + (300,) + (75,) → (60, 300, 70)
print (tuple)
print (type(tuple))

#İçiçe(Nested) Tuple oluşturulması
nested_tuple = (4, 5, 6), (7, 8, 9, 10)
print(nested_tuple)

tuple = (1, 2, 2, 2, 3, 4, 2, 3, 6, 8, 2)
print(tuple.count(2))  # 2 sayısının kaç adet olduğu
#Dictionary veri yapısı. Anahtar-değer diye eşli bilgiyle oluşur bu bilgiler noktalı virgülle ayrılır, iki bilgi arası virgülle ayrılır. Süslü parantezle tanımlanır
port = {22: "SSH", 23: "Telnet", 53: "DNS", 80: "HTTP"}
print(port)
#Değerler list, string, int ve benzeri olabilir
#Değerler tekrarlanabilir
#Değerler değiştirilebilir
#Dict, sıralamasız bir derlemedir; bu, bir dict veri yapısı içindeki item, oluşturulduğu sıradan  farklı bir sıraya yerleştirilebilir
ERP = {"AX": "MS AXAPTA", "NAV" :"MS Navision"}
print (ERP)
print (ERP['AX'])
print (ERP['NAV'])
#Dictionary yazım formatı: Dictionary ismi = {key: value}

# copy() fonksiyonu
ERPDict=ERP.copy() #Dict kopyalama
print("\n")
print (ERPDict)

ERP["Yolo"]= "Yolo ERP Software" #dict veri yapısına üye ilave etme
print ("\n",ERP) #\n içeride olduğu için olan şeye dikkat et
print("\n")
#get() fonksiyonu, dictionary’den veri almak için kullanılır.
print (ERP.get("SAP", "not found")) #dict veri yapısında değer ile sorgu, eğer değer bulunamazsa virgülden sonraki değeri döndürüyor.
print (ERP)
print (ERP.setdefault('AX', "unknown")) #key ile sorguprint ("\n")
print ("\n")
print (ERP)
print (ERP.setdefault('Dolibarr', "Dict veri yapısında mevcut değildir")) #key ile sorgu, içine ekledi
print (ERP)
print ("SAP"  in ERP) #dict veri yapısında sorgu => boolen çeviriyor. (true false)

print(ERP.keys()) #dict de keyleri listeler
print (ERP.values()) #dict de değerleri listeler

print (ERP.items()) #itemleri gösterir
print (ERP.clear()) #dict temizler. Herhangi bir değen dönmez

spanish = dict()
spanish['hello'] = 'hola'
spanish['yes'] = 'si'
spanish['one'] = 'uno'
spanish['two'] = 'dos'
spanish['three'] = 'tres'
spanish['red'] = 'rojo'
spanish['brown'] = 'marron'
spanish['green'] = 'verde'
spanish['blue'] = 'azul'
print(spanish)
print("\n")
print(spanish['two'])
print(spanish['red'])
print("\n")
dict = {'Marka': 'Toyota', 'Yıl': 2016}
print ("Marka : %s" %  dict.get('Yıl'))
print ("Value : %s" %  dict.get('Servis', "Mevcut Değil"))

import pandas as pd
data = {"isim ": ["Kaya", "Meltem", "Yağmur"], "yaş": [23, 25, 28]}
print(data)

# Python dictionary veri yapısının pandas dataFrame’e dönüştürülmesi
df = pd.DataFrame(data)
print(df)
print(type(df))

# Veri türlerinin minimum ve maksimum değerleri
import numpy as np

print(np.iinfo('int8'))
print(np.iinfo('int16'))
print(np.iinfo('int32'))
print(np.iinfo('int64'))

#Bir başka Python veri yapısı ise Küme(SET) veri yapısıdır.
#Kümeler, Matematiksel küme teorisini dikkate alan, küme işlemlerini destekleyen, benzersiz ve değişmez nesnelerin sırasız bir veri türüdür.

#Kümeler, aynı ögenin birden fazla oluşumuna izin vermediğinden, tekrarlanan değerleri önlemek için kullanılabilirler. Bir küme, bir nesneler koleksiyonudur (üyeler veya ögeler olarak adlandırılır).
#Kümedeki veriler öge veya üye olarak adlandırılırlar
s3 = set([3,2,3,4,5,6,6,6,1,1,2])
print(s3)
print(type(s3))
set_4 = {'AX','MS AXAPTA', 'SAP', 'NAV', 'oracle'}
print(set_4)
print(type(set_4))
set_4.add('Google Colab')
print(set_4)

import random

for i in range(10):
    print(random.randint(1,15)) #ondalık random sayı  üretimi

for i in range(10):
    print(random.uniform(1,15)) #float random sayi üretimi (verilen aralık ondalık olabilir)

