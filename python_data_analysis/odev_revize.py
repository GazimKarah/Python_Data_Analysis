# Ödev 2025: Keşifsel Veri Analizi Dönem Ödevi (G210100027)
# Çalıştırma ortamı: PyCharm veya herhangi bir .py script

import sys
import platform
import pandas as pd
import numpy as np
import pkg_resources

# matplotlib GUI backend seçimi (PyCharm üzerinde show() için)
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

# Bokeh (script içinde HTML dosyası oluşturmak için)
from bokeh.plotting import figure, output_file, show

# Profiling kütüphanesi
from ydata_profiling import ProfileReport

# Ek EDA & temizleme araçları
import janitor              # .clean_names()
import sweetviz            # Görsel analiz raporu
from summarytools import dfSummary

# Dataprep EDA (hata alırsanız atlatır)
try:
    from dataprep.eda import plot as dp_plot
except ImportError as e:
    print(f"dataprep import error: {e}")
    dp_plot = None

# Dağıtık DataFrame'ler
import dask.dataframe as dd

# PySpark (Java yoksa atlar)
from pyspark.sql import SparkSession

# Polars & otomatik temizleyici
import polars as pl
from datacleaner import autoclean

# Derin öğrenme kütüphanesi
import keras


# 1. Veri setini oku
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
cols = ['sepal_length','sepal_width','petal_length','petal_width','class']
KALKAN_DF = pd.read_csv(url, names=cols)

# 2. Özet bilgi
KALKAN_DF.info()
print(KALKAN_DF.describe(include='all'))

# 3. pandas versiyonu
print("Pandas version:", pd.__version__)

# 4. Yüklü paketleri listele
print([f"{pkg.key}=={pkg.version}" for pkg in pkg_resources.working_set])

# 5. Python versiyonu
print("Python version:", sys.version)

# 6–8. İlk 5 ve son 5 veri
print("Head:\n", KALKAN_DF.head())
print("Tail:\n", KALKAN_DF.tail())

# 9. Nümerik sütunlar
numeric_cols = KALKAN_DF.select_dtypes(include=[np.number]).columns.tolist()
print("Numeric columns:", numeric_cols)

# 10. Nümerik olmayanların frekans dağılımı
non_num = KALKAN_DF.select_dtypes(exclude=[np.number])
print(non_num.apply(pd.value_counts))

# 11. System/platform bilgisi
print("Platform:", platform.platform())

# 12–14. Satır, sütun sayısı ve isimleri
print("Rows:", KALKAN_DF.shape[0], "Columns:", KALKAN_DF.shape[1])
print("Column names:", KALKAN_DF.columns.tolist())

# 15–17. Eksik veri analizi
print("Null per-column:\n", KALKAN_DF.isnull().sum())
print("Total missing:", KALKAN_DF.isnull().sum().sum())

# 18–19. Eksikleri 0 ile doldurma & düşürme
KALKAN_DF_filled = KALKAN_DF.fillna(0)
KALKAN_DF_dropped = KALKAN_DF.dropna()

# 20. Tekrarlı satır sayısı
print("Duplicates:", KALKAN_DF.duplicated().sum())

# 21. Profiling raporu oluştur
profile = ProfileReport(KALKAN_DF, title="Iris Profiling")
profile.to_file("iris_report.html")

# 22. CSV kaydet ve karşılaştır
KALKAN_DF.to_csv("iris_saved.csv", index=False)
df2 = pd.read_csv("iris_saved.csv")
print("DataFrames equal?", KALKAN_DF.equals(df2))

# 23–24. Sütun seçimi, veri tipi
col = KALKAN_DF['sepal_length']
print(type(col), col.dtype)

# 25–28. loc & iloc kullanımları
print("loc row 0:", KALKAN_DF.loc[0])
print("iloc row 0:", KALKAN_DF.iloc[0])
print("loc[0,'sepal_length']:", KALKAN_DF.loc[0, 'sepal_length'])
print("slice loc[0:4]:\n", KALKAN_DF.loc[0:4, ['sepal_length','sepal_width']])

# 29. Filtreleme (sepal_length > 5)
print(KALKAN_DF[KALKAN_DF['sepal_length'] > 5])

# 30. İndeks resetleme
KALKAN_DF_reset = KALKAN_DF.reset_index(drop=True)

# 31–33. Yeni sütun ekle & sil
KALKAN_DF['sepal_area'] = KALKAN_DF['sepal_length'] * KALKAN_DF['sepal_width']
print("With new col:\n", KALKAN_DF.head())
KALKAN_DF.drop('sepal_area', axis=1, inplace=True)

# 34. Genel info tekrar
KALKAN_DF.info()

# 35. Pyjanitor ile temiz isimler
KALKAN_DF = KALKAN_DF.clean_names()

# 36–38. Versiyonlar ve temel istatistik (sadece sayısal sütunlar)
print("Pandas:", pd.__version__, "Matplotlib:", plt.matplotlib.__version__)
print("Min:\n", KALKAN_DF.min(numeric_only=True),
      "\nMax:\n", KALKAN_DF.max(numeric_only=True))
print("Mean:\n", KALKAN_DF.mean(numeric_only=True),
      "\nCount:\n", KALKAN_DF.count())

# 39–41. Pivot tablolar
print(pd.pivot_table(KALKAN_DF, values='sepal_length', index=['class']))
print(pd.pivot_table(KALKAN_DF, values='sepal_length', index=['class','sepal_width']))
print(pd.pivot_table(KALKAN_DF, values='sepal_length', index='class', aggfunc=np.sum))

# 42–47. Farklı dosya formatlarına kaydetme & sıralama işlemleri
KALKAN_DF.to_csv("iris_output.csv", index=False)
KALKAN_DF.to_excel("iris_output.xlsx", index=False)
KALKAN_DF.to_html("iris_output.html", index=False)
KALKAN_DF.to_json("iris_output.json", orient='records')
KALKAN_DF.to_csv("iris_output.txt", sep='\t', index=False)

print("Sorted asc:\n", KALKAN_DF.sort_values('sepal_length').head())
print("Sorted desc:\n", KALKAN_DF.sort_values('sepal_length', ascending=False).head())
print("Multi-sort:\n", KALKAN_DF.sort_values(
    ['sepal_length','sepal_width'], ascending=[True,False]).head())

# 51. Rastgele örnekleme
print("Sample 5:\n", KALKAN_DF.sample(5))

# 52–58. Matplotlib grafikler
plt.scatter(KALKAN_DF['sepal_length'], KALKAN_DF['sepal_width'])
plt.title('Scatter: Sepal Length vs Width')
plt.show()

plt.hist(KALKAN_DF['sepal_length'])
plt.title('Histogram: Sepal Length')
plt.show()

counts = KALKAN_DF['class'].value_counts()
plt.bar(counts.index, counts.values)
plt.title('Bar: Class Distribution')
plt.show()

counts.plot.pie(autopct='%1.1f%%', title='Pie: Class Distribution')
plt.show()

sns.heatmap(KALKAN_DF.corr(numeric_only=True), annot=True)
plt.title('Heatmap: Correlation')
plt.show()

sns.stripplot(x='class', y='sepal_length', data=KALKAN_DF)
plt.title('Stripplot')
plt.show()

sns.swarmplot(x='class', y='sepal_length', data=KALKAN_DF)
plt.title('Swarmplot')
plt.show()

# 59–60. Keras versiyonu
print("Keras version:", keras.__version__)

# 61. İki sütunlu CSV import
df_two = pd.read_csv(url, names=cols, usecols=['sepal_length','sepal_width'])
print(df_two.head())

# 62. math_ops.py modülü oluşturma
math_code = """
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
"""
with open('math_ops.py', 'w') as f:
    f.write(math_code)

# 63. Sweetviz raporu (hata alırsa atla)
try:
    sv_report = sweetviz.analyze(KALKAN_DF)
    sv_report.show_html('sweetviz_report.html')
except Exception as e:
    print(f"Sweetviz error: {e}")

# 64. summarytools analizi
dfSummary(KALKAN_DF)

# 65. Bokeh interaktif grafik (scatter() kullanarak)
output_file("iris_plot.html", title="Sepal Length vs Width")
p = figure(title="Sepal Length vs Width")
p.scatter(KALKAN_DF['sepal_length'], KALKAN_DF['sepal_width'], size=6)
show(p)

# 66. Dask dataframe
ddf = dd.from_pandas(KALKAN_DF, npartitions=2)
print(ddf.head())

# 67. PySpark dataframe (Java yoksa bildiri)
try:
    spark = SparkSession.builder.appName("IrisEDA").getOrCreate()
    spark_df = spark.createDataFrame(KALKAN_DF)
    spark_df.show(5)
except Exception as e:
    print(f"PySpark error (check JAVA_HOME): {e}")

# 68. Dataprep EDA
if dp_plot:
    dp_plot(KALKAN_DF)
else:
    print("dataprep EDA skipped.")

# 69. Polars kullanımı
pl_df = pl.from_pandas(KALKAN_DF)
print(pl_df.head())

# 70. DataCleaner otomatik temizleme
df_clean = autoclean(KALKAN_DF.copy())
print(df_clean.head())

# 71–73. Melt, boş doldurma, aykırı değer çıkarma
df_melt = KALKAN_DF.melt(
    id_vars=['class'],
    value_vars=['sepal_length','sepal_width'],
    var_name='measurement',
    value_name='value'
)
print(df_melt.head())

KALKAN_DF.fillna(KALKAN_DF.mean(numeric_only=True), inplace=True)
q1 = KALKAN_DF['sepal_length'].quantile(0.25)
q3 = KALKAN_DF['sepal_length'].quantile(0.75)
IQR = q3 - q1
KALKAN_DF = KALKAN_DF[~(
    (KALKAN_DF['sepal_length'] < (q1 - 1.5*IQR)) |
    (KALKAN_DF['sepal_length'] > (q3 + 1.5*IQR))
)]

# 75. PyHadoop örneği
try:
    import pyhadoop
    print("pyhadoop loaded")
except ImportError:
    print("pyhadoop kütüphanesi yüklü değil")
#Çok hata oluştu ondan böyle yaptım
