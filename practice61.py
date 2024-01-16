n = int(input("Введіть значення n"))#22
suma = 0
for i in range(n):
    suma = suma + (i/(2*i + 1)) ** .5
print(suma)


