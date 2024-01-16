def print_triangle(C, W):
    for i in range (W):
        n = int(W-i)
        print(C*n)
print("Приклад")
print_triangle("x", 6)
C_p = input("Символ")
W_p = int(input("Основа трикутника"))
print_triangle(C_p, W_p)


