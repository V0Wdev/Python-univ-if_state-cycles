print('x=')
x = float(input())
print('y=')
y = float(input())
с = x**2 + y**2
if с >=4 and с <=9:
    if -x <= y:
        print('belongs')
    else:
        print('do not belongs')
else:
    print('do not belongs')