import random

def random_matrix(n, a, b):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(random.randint(a, b))
    return matrix

n = int(input("Розмір матриці "))
a = int(input("від "))
b = int(input("до "))

matrix = random_matrix(n, a, b)
print(matrix)

def get_special_suma(n, matr):
    ster = []
    for j in range(n):
        jjj = matr[j]
        print(jjj)
        ser = n - j
        suma = 0
        s = 0
        while s in range(ser-1):
            suma = suma + jjj[s]
            if s == (ser-2):
                ster.append(suma)
            s = s+1

    print("Спеціальні суми", ster)
    specail_sum = max(ster)
    return specail_sum

print("Максимальна", get_special_suma(n,matrix))



