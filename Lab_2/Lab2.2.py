import array as arr
import random
import matplotlib.pyplot as plt
import math
import numpy as np

k=31
a=16807
s=4
step=4
count=20
m=2**k
sum_Mat=0 #матожидание


a=(2**s)+3
x_start=random.randint(0,m)/m
#x_start=random.(0,m)

values=arr.array('d',[x_start])


for i in range(1, count):
    x=(a*values[i-1]*m%m)
    x=x/m
    sum_Mat+=x
    print(x)
    values.append(x)

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

x = np.array([x for x in range(count)])
y = np.array(values)

M=(1/count)*sum_Mat
D=sum(list(map(lambda x: (x-M) ** 2,values)))/count  #Дисперсия
sigma=math.sqrt(D) #среднеквадратичное отклонение

print(f"Количество чисел равно {count}")
print("---------------")
print("Статистический тест")
print("Мат. ожидание:")
print(M)
print("Дисперсия:")
print(D)
print("Ср.квадратичное:")
print(sigma)

leftBorder = M - sigma
rightBorder = M + sigma
idealNumbers = [x for x in values if x>leftBorder and x<rightBorder]
perc = len(idealNumbers)/count * 100
print("---------------")
print("Частотный тест:")
print(f"{perc:.4f}% значений попали в отрезок ({leftBorder:.4f};{rightBorder:.4f})")
#plt.hist([values,idealNumbers], color = ['blue', 'violet'], edgecolor = 'black',
     #  bins = int(2))
plt.hist(values, color = ['orange'], edgecolor = 'white', bins=int(step))
plt.title('Распределение случайных чисел при количестве чисел равным '+str(count))
plt.xlabel('Отрезок')
plt.ylabel('Количесво')
# Покажем окно с нарисованным графиком
plt.show()