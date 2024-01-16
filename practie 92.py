import random

mens = {}
for i in range(10):
    age = random.randint(18, 60)
    weight = random.randint(45, 100)
    mens[age] = weight

print(mens)
print("Вік   маса")
for age, weight in mens.items():
    print(f"{age}   {weight}")

suma_weight = 0
for m in mens:
    suma_weight = suma_weight + mens[m]
print("Загальна маса", suma_weight)

