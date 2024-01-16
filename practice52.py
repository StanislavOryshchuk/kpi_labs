
num = int(input())
if num<2:
    print("Введіть число більше 2")
n = num
i = 2
res = 1
while i<n:
    polka = num%i
    if polka == 0:
        res = i
        break
    else:
        res = num

    i = i+1

print(res)

