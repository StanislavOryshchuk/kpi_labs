print("Введіть x")
x = int(input())
print("Введіть а")
a = int(input())
xdt = x/a
if xdt > 0:
    y = ((x^2)+a)^3
elif xdt < 0:
    d = float(2/3)
    y = d + a
else:
    y = ((2*x^2)**(1./3.)) + a
print(y)
