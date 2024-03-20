from pulp import LpVariable, LpProblem, LpMaximize, value
import time

start = time.time()
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
problem = LpProblem('0', LpMaximize)
problem += x1*2+x2*1.5, "Функция цели"
problem += x1*20+x2*10<=60, "1"
problem += x1+x2<=40, "2"
problem.solve()
print("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print("кол-во штук:")
print(value(problem.objective))
stop = time.time()
print ("Время :")
print(stop - start)
