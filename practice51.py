x0=1
xk=2.2
dx=0.2
b=3.2
x = x0
while x < xk:
    y = 9*(x**3 + b**3)*x
    print("x=", x, "   ", "y=", y)
    x = x+dx

