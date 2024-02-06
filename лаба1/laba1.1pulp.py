from pulp import LpVariable, LpProblem, LpMinimize, value

import time

start = time.time()
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)
x4 = LpVariable("x4", lowBound=0)
x5 = LpVariable("x5", lowBound=0)
x6 = LpVariable("x6", lowBound=0)
x7 = LpVariable("x7", lowBound=0)
problem = LpProblem('0', LpMinimize)
problem += 1.8* x1+x2+0.28*x3+3.4*x4+2.9* x5+0.5*x6+0.1*x7, "Функция цели"
problem += 180* x1+190*x2+30*x3+10*x4+260* x5+130*x6+21* x7>=118, "1"
problem += 20* x1+3*x2+40*x3+865*x4+310* x5+30*x6+2* x7 >=56, "2"
problem += 50*x3+6*x4+20* x5+650*x6+200* x7>=500, "3"
problem += 9* x1+10*x2+7*x3+12*x4+60* x5+20*x6+10* x7 >=8, "4"
problem.solve()
print("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print("Стоимость:")
print(value(problem.objective))
stop = time.time()
print ("Время :")
print(stop - start)

