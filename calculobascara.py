import math

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

delta = b**2 - 4*a*c

if delta == 0:
    x1 = (-b + math.sqrt(delta))/(2*a)
    print("Resultante nao pode ser igual a zero !!")
else:
    if delta < 0:
        print("Esta equaçao nao existe raizes reais.")
    else:
        x1 = (-b + math.sqrt(delta)) /(2*a)
        x2 = (-b - math.sqrt(delta)) /(2*a)
        print("O valor da solução é:",x1,",",x2,".")



