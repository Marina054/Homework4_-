# Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
# Найдите ее среднее значение и дисперсию.
import numpy as np
a = 200
b = 800
t = [200, 800]
print(np.average(t))    # 500
Disp = (a - b)**2 / 12
print(Disp)     # 30000