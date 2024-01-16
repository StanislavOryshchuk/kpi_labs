import random
m = int(input("Кількість випадкових чисел: "))
k = int(input("Кількість чисел в рядку виведення:"))#3≤k≤10
a = int(input()) #[-1000, 500]
b = int(input())

for p in range(m):
    rn = random.randrange(a, b)
    print(rn, end=" ")
    if (p + 1) % k == 0:
        print()
    else:
        continue


