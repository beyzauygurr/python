#CLASSES AND OBJECTS

class my_class:
    x=5
    
p=my_class()
print(p.x)  
print(my_class.x)  

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    

p1 = Person("beyza", 23)

print(p1.name)
print(p1.age)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

p1.age=20
print(p1)

#car class

# Araba sınıfı tanımlama
class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.hiz = 0
    
    def hizlan(self, artis):
        self.hiz += artis
    
    def dur(self):
        self.hiz = 0

# Araba nesnesi oluşturma
araba1 = Araba("Mercedes", "C180", 2020)

# Araba özelliklerine erişme ve metodları kullanma
print(araba1.marka)  # Mercedes
print(araba1.model)  # C180
print(araba1.yil)    # 2020

araba1.hizlan(50)
print("Arabanın hızı:", araba1.hiz)  # Arabanın hızı: 50

araba1.dur()
print("Arabanın hızı:", araba1.hiz)  # Arabanın hızı: 0





























