# Ödev 2025: Keşifsel Veri Analizi Dönem Ödevi (G210100027) Gazi Muhammed Kalkan
#NOT: Burada kullanılan bazı kütüphanelerin birbiri arasında sürümsel çakışmaları söz konusudur doğru sürümlerle çalıştırınız.

# Gerekli kütüphane importları
import pandas as pd
import numpy as np
import sys
import setuptools
import platform
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport
import janitor
import sweetviz
from summarytools import dfSummary
from bokeh.plotting import figure, output_notebook, show
import dask.dataframe as dd
from pyspark.sql import SparkSession
from dataprep.eda import plot as dp_plot
import polars as pl
from datacleaner import autoclean
from IPython.core.display import display
# Keras importu (task 59)
import keras

# 1. Veri setini pandas DataFrame ile okuyunuz.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
cols = ['sepal_length','sepal_width','petal_length','petal_width','class']
SOYAD_DF = pd.read_csv(url, names=cols)

# 2. DataFrame verileri ile ilgili özet bilgileri ekranda gösteriniz.
SOYAD_DF.info()
SOYAD_DF.describe(include='all')

# 3. pandas kütüphanesi versiyonu bulunuz.
print("Pandas version:", pd.__version__)

# 4. Install edilen kütüphaneleri listeleyiniz.
installed = setuptools.working_set
print([f"{i.key}=={i.version}" for i in installed])

# 5. Python Yazılımın Versiyonunu bulunuz.
print("Python version:", sys.version)

# 6. Veri setindeki ilk 5 veriyi listeleyiniz.
print(SOYAD_DF.head())

# 7. Veri setindeki son 5 veriyi listeleyiniz.
print(SOYAD_DF.tail())

# 8. Veri setindeki bütün verileri listeleyiniz.
print(SOYAD_DF)

# 9. Veri setindeki nümerik alanları listeleyiniz.
numeric_cols = SOYAD_DF.select_dtypes(include=[np.number]).columns.tolist()
print("Numeric columns:", numeric_cols)

# 10. Veri setindeki nümerik olmayan alanların frekans dağılımını analiz ediniz.
non_numeric = SOYAD_DF.select_dtypes(exclude=[np.number])
print(non_numeric.apply(pd.value_counts))

# 11. System Kütüphanesi versiyonunu bulunuz.
print("Platform version:", platform.platform())

# 12. Veri setindeki toplam veri sayısını bulunuz.
print("Total rows:", SOYAD_DF.shape[0])

# 13. Veri setindeki toplam sütun sayısını bulunuz.
print("Total columns:", SOYAD_DF.shape[1])

# 14. Veri setindeki sütun isimlerini bulunuz.
print(SOYAD_DF.columns.tolist())

# 15. Veri setindeki eksik verileri bulunuz.
print(SOYAD_DF.isnull())

# 16. Her bir sütundaki eksik veri sayısını bulunuz.
print(SOYAD_DF.isnull().sum())

# 17. Bütün sütunlardaki toplam eksik veri sayısını bulunuz.
print("Total missing:", SOYAD_DF.isnull().sum().sum())

# 18. Eksik verilerin yerine "0 - sıfır" yazınız.
SOYAD_DF_filled = SOYAD_DF.fillna(0)

# 19. Eksik verileri dataFrame'den çıkarınız.
SOYAD_DF_dropped = SOYAD_DF.dropna()

# 20. Tekrarlı verilerin sayısını bulunuz.
print("Duplicate rows:", SOYAD_DF.duplicated().sum())

# 21. ydata_profiling ile otomatik rapor hazırlayınız.
profile = ProfileReport(SOYAD_DF, title="Profiling Report")
profile.to_file("iris_report.html")

# 22. CSV dosyası olarak kaydedip karşılaştırınız.
SOYAD_DF.to_csv("iris_saved.csv", index=False)
df2 = pd.read_csv("iris_saved.csv")
print("DataFrames equal?", SOYAD_DF.equals(df2))

# 23. DataFrame'deki herhangi bir sütunu ekrana alınız ve veri tipini sorgulayınız.
col = SOYAD_DF['sepal_length']
print(col, type(col))

# 24. Sütunun Class'ını sorgulayınız.
print(col.dtype)

# 25. loc ile indeks etiketi sorgusu (örn. ilk satır için index=0)
print(SOYAD_DF.loc[0])

# 26. iloc ile indeks numarası sorgusu
print(SOYAD_DF.iloc[0])

# 27. loc ile satır ve sütun seçiniz
print(SOYAD_DF.loc[0, 'sepal_length'])

# 28. loc ile dilimleme (örnek)
print(SOYAD_DF.loc[0:4, ['sepal_length','sepal_width']])

# 29. Filtreleme (sepal_length > 5 olanlar)
print(SOYAD_DF[SOYAD_DF['sepal_length'] > 5])

# 30. İndeksi sıfırlayınız.
SOYAD_DF_reset = SOYAD_DF.reset_index(drop=True)

# 31. Yeni bir sütun ilave ediniz.
SOYAD_DF['sepal_area'] = SOYAD_DF['sepal_length'] * SOYAD_DF['sepal_width']

# 32. Bir sütunu geçici siliniz.
print(SOYAD_DF.drop('sepal_area', axis=1))

# 33. Bir sütunu kalıcı siliniz.
SOYAD_DF.drop('sepal_area', axis=1, inplace=True)

# 34. DataFrame hakkında genel bilgi
print(SOYAD_DF.info())

# 35. Pyjanitor ile veri temizleme (clean_names örneği)
SOYAD_DF = SOYAD_DF.clean_names()

# 36. Pandas versiyonu
print(pd.__version__)

# 37. Matplotlib versiyonu
import matplotlib
print(matplotlib.__version__)

# 38. min, max, mean, count değerleri
print(SOYAD_DF.min())
print(SOYAD_DF.max())
print(SOYAD_DF.mean())
print(SOYAD_DF.count())

# 39. Tek indeksli pivot table
print(pd.pivot_table(SOYAD_DF, values='sepal_length', index=['class']))

# 40. Çok indeksli pivot table
print(pd.pivot_table(SOYAD_DF, values='sepal_length', index=['class','sepal_width']))

# 41. aggfunc=np.sum ile pivot table
print(pd.pivot_table(SOYAD_DF, values='sepal_length', index='class', aggfunc=np.sum))

# 42. CSV olarak kaydetme
SOYAD_DF.to_csv("iris_output.csv", index=False)

# 43. Excel olarak kaydetme
SOYAD_DF.to_excel("iris_output.xlsx", index=False)

# 44. HTML olarak kaydetme
SOYAD_DF.to_html("iris_output.html", index=False)

# 45. JSON olarak kaydetme
SOYAD_DF.to_json("iris_output.json", orient='records')

# 46. TXT olarak kaydetme (tab ayraçlı)
SOYAD_DF.to_csv("iris_output.txt", sep='\t', index=False)

# 47. Bir sütunu küçükten büyüğe sıralayınız.
print(SOYAD_DF.sort_values('sepal_length'))

# 48. Bir sütunu büyükten küçüğe sıralayınız.
print(SOYAD_DF.sort_values('sepal_length', ascending=False))

# 49. İki sütunu küçükten büyüğe sıralayınız.
print(SOYAD_DF.sort_values(['sepal_length','sepal_width']))

# 50. İki sütunu büyükten küçüğe sıralayınız.
print(SOYAD_DF.sort_values(['sepal_length','sepal_width'], ascending=[False,False]))

# 51. 5 veriyi rastgele listeleyiniz.
print(SOYAD_DF.sample(5))

# 52. Scatter plot
plt.figure()
plt.scatter(SOYAD_DF['sepal_length'], SOYAD_DF['sepal_width'])
plt.title('Scatter: Sepal Length vs Width')
plt.show()

# 53. Histogram
plt.figure()
plt.hist(SOYAD_DF['sepal_length'])
plt.title('Histogram: Sepal Length')
plt.show()

# 54. Bar chart
plt.figure()
counts = SOYAD_DF['class'].value_counts()
plt.bar(counts.index, counts.values)
plt.title('Bar: Class Distribution')
plt.show()

# 55. Pie chart
plt.figure()
counts.plot.pie(autopct='%1.1f%%', title='Pie: Class Distribution')
plt.show()

# 56. Heat Map (korelasyon matrisi)
plt.figure(figsize=(6,5))
sns.heatmap(SOYAD_DF.corr(), annot=True)
plt.title('Heatmap: Correlation')
plt.show()

# 57. Stripplot (Seaborn)
plt.figure()
sns.stripplot(x='class', y='sepal_length', data=SOYAD_DF)
plt.title('Stripplot')
plt.show()

# 58. Swarmplot (Seaborn)
plt.figure()
sns.swarmplot(x='class', y='sepal_length', data=SOYAD_DF)
plt.title('Swarmplot')
plt.show()

# 59. Keras kütüphanesini yükleyiniz. (Zaten import edildi)

# 60. Keras versiyonunu bulunuz.
print("Keras version:", keras.__version__)

# 61. CSV dataset'den sadece iki sütunu import ediniz.
df_two = pd.read_csv(url, names=cols, usecols=['sepal_length','sepal_width'])
print(df_two.head())

# 62. İki sayıyı toplamak ve çarpmak için bir modül oluşturunuz.
# math_ops.py dosyası oluşturma
t_math = '''
def add(a, b):
    """İki sayıyı toplar"""
    return a + b

def multiply(a, b):
    """İki sayıyı çarpar"""
    return a * b
'''
with open('math_ops.py', 'w') as f:
    f.write(t_math)

# 63. Sweetviz ile analiz yapınız.
sv_report = sweetviz.analyze(SOYAD_DF)
sv_report.show_html('sweetviz_report.html')

# 64. summarytools ile analiz yapınız.
dfSummary(SOYAD_DF)

# 65. Bokeh ile interaktif grafik örneği
output_notebook()
p = figure(title="Sepal Length vs Width")
p.circle(SOYAD_DF['sepal_length'], SOYAD_DF['sepal_width'])
show(p)

# 66. DASK kullanınız.
ddf = dd.from_pandas(SOYAD_DF, npartitions=2)
print(ddf.head())

# 67. pySpark kullanınız.
spark = SparkSession.builder.appName("IrisEDA").getOrCreate()
spark_df = spark.createDataFrame(SOYAD_DF)
spark_df.show(5)

# 68. dataprep kullanınız.
dp_plot(SOYAD_DF)

# 69. Polars kullanınız.
pl_df = pl.from_pandas(SOYAD_DF)
print(pl_df.head())

# 70. datacleaner kullanınız.
df_clean = autoclean(SOYAD_DF.copy())
print(df_clean.head())

# 71. Data wrangling örneği (melt)
df_melt = SOYAD_DF.melt(id_vars=['class'], value_vars=['sepal_length','sepal_width'], var_name='measurement', value_name='value')
print(df_melt.head())

# 72. Data cleaning örneği (boş değer doldurma)
SOYAD_DF.fillna(SOYAD_DF.mean(), inplace=True)

# 73. Data cleansing örneği (aykırı değer çıkarma)
q1 = SOYAD_DF['sepal_length'].quantile(0.25)
q3 = SOYAD_DF['sepal_length'].quantile(0.75)
IQR = q3 - q1
SOYAD_DF = SOYAD_DF[~((SOYAD_DF['sepal_length'] < (q1 - 1.5 * IQR)) | (SOYAD_DF['sepal_length'] > (q3 + 1.5 * IQR)))]

# 74. pyspark tekrar gösterimi (tekrarlı görev)
# Yukarıda spark kullanıldı.

# 75. pyhadoop kullanımı (örnek kütüphane)
try:
    import pyhadoop
    print("pyhadoop loaded")
except ImportError:
    print("pyhadoop kütüphanesi yüklü değil")
