from scipy import fft
from math import pi
import numpy as np
from numpy import arange, cos
import matplotlib.pyplot as plt

A=3
dt=1
fi=pi/8
T=100
k=arange(0,1023)
step=1

s=(2*pi*(k-1)*dt)/T
print (s)

x1=A*cos(s+fi)
print (x1)
y=fft.fft(x1)
print(y)
F=fft.ifft(y)
print(F)
f=arange(0,len(y))/len(y)
print(f)

# Отображение графиков
plt.figure(figsize=(15, 15)) # размер графика

y_abs=np.abs(y)
plt.subplot(2, 2, 1)

# !!! Текущая ячейка - 1 (левый верхний график)
#plt.scatter(f, x1, label = 'data') # точечный график по x_numpy, y_numpy
plt.plot( f, x1, linestyle='dashed', color="orange") # Функция сигнала
plt.grid(color="gainsboro") # Сетка
plt.legend(loc='best', fontsize=12) 
plt.title("Функция сигнала")

plt.subplot(2, 2, 2)
fig = plt.gcf() # Взять текущую фигуру
fig.set_size_inches(15, 15) # Задать размеры графика

plt.plot( f, F, linestyle='dashed', color="orange") # Обратное преобразование Фурье
plt.grid(color="gainsboro") # Сетка
plt.legend(loc='best', fontsize=12) 
plt.title("Обратное преобразование Фурье")

plt.subplot(2, 2, 3)
fig = plt.gcf() # Взять текущую фигуру
fig.set_size_inches(15, 15) # Задать размеры графика

plt.plot( f, y, linestyle='dashed', color="orange") # Прямое преобразование Фурье
plt.grid(color="gainsboro") # Сетка
plt.legend(loc='best', fontsize=12) 
plt.title("Прямое преобразование Фурье")

fig = plt.gcf() # Взять текущую фигуру
fig.set_size_inches(15, 15) # Задать размеры графика

# Покажем окно с нарисованным графиком
plt.show()