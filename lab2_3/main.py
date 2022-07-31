from random import *
mas=[]
print('')
N=int(input())
for i in range(N+10):
    mas.append(randint(0, 100))
print(mas)
a = mas[0]
mas[0] = mas[-1]
mas[-1] = a
print(mas)
