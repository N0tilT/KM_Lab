from cvxopt.modeling import variable, op
import time

start = time.time()
x = variable(7, 'x')
z=(1.8* x[0]+x[1]+0.28*x[2]+3.4*x[3]+2.9* x[4]+0.5*x[5]+0.1*x[6])#Функция цели
mass1 = (-(180* x[0]+190*x[1]+30*x[2]+10*x[3]+260* x[4]+130*x[5]+21* x[6])<=-118) #"1"
mass2 =(- (20* x[0]+3*x[1]+40*x[2]+865*x[3]+310* x[4]+30*x[5]+2* x[6]) <=-56)# "2"
mass3 =(- (50*x[2]+6*x[3]+20* x[4]+650*x[5]+200* x[6])<=-500) # "3"
mass4 =(- (9* x[0]+10*x[1]+7*x[2]+12*x[3]+60* x[4]+20*x[5]+10* x[6] )<=-8) # "4"
x_non_negative = (x >= 0) #"5"
problem =op(z,[mass1,mass2,mass3,mass4,x_non_negative])
problem.solve(solver='glpk')
problem.status
print ("Стоимость:")
print(abs(problem.objective.value()[0]))
print ("Результат:")
print(x.value)
stop = time.time()
print ("Время :")
print(stop - start)