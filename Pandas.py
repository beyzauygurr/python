
"""
Pandas is a Python library.

Pandas is used to analyze data.
"""
import pandas
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)


# Örnek bir veri çerçevesi oluşturalım
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Jake'],
    'Age': [28, 35, 45, 30, 25],
    'Gender': ['M', 'F', 'M', 'F', 'M']
}

df = pd.DataFrame(data)

# Veri çerçevesinden rastgele bir örnekleme alalım (varsayılan olarak bir satır)
random_sample = df.sample()
print("Rastgele örnek satır:")
print(random_sample)

# Belirli bir boyutta rastgele bir örnekleme almak için 'n' parametresini kullanabilirsiniz
random_sample_size = df.sample(n=3)  # 3 satır alalım
print("\nRastgele örnek satırlar (3 satır):")
print(random_sample_size)
