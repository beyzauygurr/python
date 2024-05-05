
"""
NumPy is a Python library.

NumPy is used for working with arrays.

NumPy is short for "Numerical Python".

"""
import numpy as np

array=np.array([1,2,3,4])
print(array)
print(type(array))


arr = np.array(42)
print(arr)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

dizi=np.arange(1,11)

print(dizi)
print(dizi.size) #dizi boyut
print(dizi.dtype) #dizi veri tipi
print(dizi.ndim) #dizinin boyut sayısı
print(np.min(dizi)) #en küçük eleman
print(np.max(dizi)) #en büyük eleman
print(np.mean(dizi)) #ortalama
print(np.std(dizi)) #standart sapma























