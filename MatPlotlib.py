
import matplotlib.pyplot as plt
import numpy as np

# Örnek veri oluşturalım
x = np.linspace(0, 10, 100)  # 0 ile 10 arasında 100 adet x değeri oluşturalım
y = np.sin(x)  # x'in sinüs fonksiyonunu alalım

# Grafik çizelim
plt.plot(x, y, label='sin(x)', color='blue', linestyle='-')  # sinüs grafiğini çizelim
plt.title('Sinüs Fonksiyonu')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()  # Grafikteki etiketleri gösterelim
plt.grid(True)  # Izgara ekleyelim
plt.show()
