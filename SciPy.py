# -*- coding: utf-8 -*-
"""
SciPy is a scientific computation library that uses NumPy underneath.

SciPy stands for Scientific Python.

"""

from scipy import stats
import numpy as np

# Normal dağılıma sahip bir veri kümesi oluşturalım (örnek veri)
np.random.seed(0)  # Tekrarlanabilirlik için seed ayarlayalım
mu, sigma = 0, 1  # Ortalama ve standart sapma
sample_data = np.random.normal(mu, sigma, 1000)

# Örneklem alalım
sample = np.random.choice(sample_data, size=100, replace=False)  # 100 elemanlı örneklem, tekrar yok

print("Örneklem büyüklüğü:", len(sample))
print("Örneklem istatistikleri:")
print("Ortalama:", np.mean(sample))
print("Standart sapma:", np.std(sample))

