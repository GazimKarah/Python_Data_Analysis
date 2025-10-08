
import matplotlib.pyplot as plt
import pandas as pd


sayılar = pd.Series([0, 1, 5, 6, 7, 8, 90, 104, 9, 160, 250,
46, 19], name='Sayı Listesi ')

print (sayılar)

#Web sitesinden CSV dosyasının okunması
df =  pd.read_csv('https://raw.githubusercontent.com/QuantLet/MVA/master/QID-1226-MVAportfol/apple.csv', index_col = "Date", parse_dates=True)

#İndeks Dateolarak belirlenmiştir
#parse_dates=True, tarihle ilgili veriler olduğunu belirtmektedir
print (df)

# veri seti indeks sıralama tarihe göre
df = df.sort_index()
print("\n")
print(df)

print("\n")
print("dataFrame detayları: \n")
print(df.info()) # veriler ile ilgili özet

print("dataFrame kısa detay: \n")
print(df.info(verbose=False)) # ayrıntılı detay false olarak değiştirildi

print("\n")

# dataFrame'deki null değerlerin-verilerin sayısı
print("dataframe detayları :")
print(df.info(show_counts=True))

print("\n")

# dataFrame'deki null değerlerin-verilerin sayısının kaldırılması
print("dataframe detayları :")
print(df.info(show_counts=False))

print("\n")

# indeks sıralama
print(df.sort_index(axis = 0))
#axis=0 satırları göstermektedir

print("\n")

# sütunlar için indeks sıralama, axis=1 sütunlarıgöstermektedir
print(df.sort_index(axis=1))

print("\n")

# pandas.to_markdown() metodu kullanımı
markDown = df.to_markdown()
print(markDown)

print("\n")

# indeksin "ascending = False" ile büyükten küçüğe sıralanması
df = df.sort_index(ascending=False)
#ascending=False
print(df)

print("\n")

# DataFrame’in «Close» Sütunortalamasının hesabı
#2009 yılı hisse senedi kapanış fiyat ortalaması
# df.loc['2009', 'Close'].mean()
#loc location dan gelmektedir.
print ("Ortalama Hisse Kapanış Fiyatı: ",df.loc['2009', 'Close'].mean())

print("\n")

#Pandas, “partial string slice” (örneğin '1999-Jan':'2009-Jan')
# yaparken indeksin artan (monotonic increasing) olmasını bekler.
# Bu yüzden aşağıdaki kod çalışması için  tekrar indecleme gerekir
df = df.sort_index()
print ('On yıllık ortalama kapanış fiyatı:')
print("\n")
print (df.loc['1999-Jan':'2009-Jan', 'Close'].mean())

print("\n")
# dataframe’deki axis = 0 ve axis= 1
# DataFramesütunlarındaki, 'Low" ve 'High' değerlerin toplanması
print(df[['Low', 'High']].sum(axis=0))

#Matplotlib kütüphanesi:
#Çeşitli formatlarda grafik çizmek için kullanılan Python 2Dçizim kütüphanesi
#matplotlib kütüphanesinin MATLAB programına benzer özellikleri vardır
#Çizgi grafikleri, dağılım grafikleri, çubuk grafikler,
#histogramlar, pasta grafikler(line plots, scatter plots, barcharts, histograms, pie charts) kullanılabilir.
data_frame = df.loc['1999-Jan':'2009-Jan', ['Close']]
print(data_frame)
data_frame.plot()
plt.show()

# yıllara göre grafik, Hacim için veri görselleştirme
data_frame = df.loc['1999-Jan':'2009-Jan', ['Volume']]
data_frame.plot()
plt.show()

print("\n")

# 1999-Dec diye değişiklik yapılır ise oradan itibaren çizecektir.
data_frame = df.sort_index().loc['1999-Jan':'2009-Jan', ['Close']]
data_frame.plot()
plt.show()

print("\n")

#İlk 5 verinin Listesi
print (df.head())# ilk 5 veri veya
print("\n")
print (df.head(5)) # ilk 5 veri

# Bütün observation-kayıtların listesi(ilk kayıt hariç)
print()
print(df.tail(-1))

#sütunlardaki veri türünün incelenmesi
print
print (df.dtypes)

print (df.columns) # dataFrame’deki sütun isimleri

print #satır etiketleri ve sütun isimleri
print (df.axes)

# dataframe’deki toplam veri sayısı
print
print ("toplam veri sayısı: ", df.size) # dataFrame veri sayısı

#DATA FRAME METODLARI
print() #dataFrame sayısal alanlar için temel istatistikler
print (df.describe())

print()#dataFrame sayısal alanlar için temel istatistikler transpozesi
print (df.describe().T)

print  # maksimum veri
print(df.max())

print # Minimum veri
print (df.min())

print()  # ortalama kayıt
print(df.mean())
# medyan ortanca değer
print("\n")
print(df.median())
# standart sapma
print("\n")
print(df.std())

print() # ortalama kapanış
print("dataframe "'Close'" sütunu ortalama ")
print (df.Close.mean())

#Ayrıca .median .std gibi komutlar da bu noktada çalışır.

#ÖNEMLİ NOT: .veri. yazımı (attribute) aradaki "veri" kelimesi
#Sütun adı, geçerli bir Python değişken adı (harf/alt çizgi ile başlayıp,
# içinde sadece harf, rakam veya alt çizgi barındıran) olmalı.
#Aynı adla Pandas’ın DataFrame veya Series içinde zaten var olan
# bir metod/özellik (ör. df.index, df.mean vb.) çakışmadığı durumda
# Çalışır onun dışında (key) yöntemiyle nokta olmaksızın df["veri"] yaparsa
# Sistem onu key gibi alır ve her durumda çalışır.

print("\n")

# Open kullanılarak verilerin gruplandırılması
df_Open = df.groupby(['Open'])
print(df_Open)
print(df_Open.first())

print("\n")

# dataframe’deki satır ve sütun sayısı
print (df.shape)

#Bir observation’da – kayıtta veya satırda, veri mevcut
# değil ise bunların ekrana getirilmesi – missing data(eksik veri) bulunması
print (df[df.isnull().any(axis=1)].head())

print(" toplam satır sayısı: ", len(df))

# iloc[] ile satır seçilir
print(df.iloc[399])
# loc[] ile sütun seçilir