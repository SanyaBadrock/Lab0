import math

#ввод значений
print("Подставьте значения в уравнение вида:")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

#подсчет дискриминанта
D = b ** 2 - 4*a*c
print("Дискриминант D = %.2f" % D)
if D > 0:
    xpervoe = (-b + math.sqrt(D)) / (2 * a)
    xvtoroe = (-b - math.sqrt(D)) / (2 * a)
    print("xpervoe = %.2f \nxvtoroe = %.2f" % (xpervoe, xvtoroe))

elif D == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("х ∈ ∅")