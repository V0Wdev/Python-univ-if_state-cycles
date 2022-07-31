import math
from math import *
print("x:")
x = float(input())
print("a:")
a = float(input())
if x < 0:
    y = sqrt((((a*a)**(1/3)) - ((x*x)**(1/3))) ** 3)
else:
    y = a + sqrt(x**3/(2*a - x))
print(y)