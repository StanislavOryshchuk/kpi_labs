import random
n = int(input("Кількість випадкових елементів:"))
a = int(input("згенерованих на інтервалі від: "))
b = int(input("до: "))
elements = []
for i in range(n):
    random_num = random.randrange(a,b)
    elements.append(random_num)
print("Масив",elements)#кількість елементів в діапазоні A B (з клавіатури)

print("Пункт 1")
A = int(input("А: "))
B = int(input("B: "))
counter_good_elements = 0
for i in range(len(elements)):
    check_el = elements[i]
    if check_el >= A and check_el <= B:
        counter_good_elements+=1
print(f"Кількість елементів в діапазані від А до В: {counter_good_elements}")# суму елементів списку розташованих після максимального

print("Пункт 2 ")
max_element = max(elements)
index_max =elements.index(max_element)
after_max = elements[index_max+1:]
print(f"Максимальний елемент: {max_element}")
print(f"Елементи розташовані після максимального: {after_max}")

sum_after_max = 0
for i in range(len(after_max)):
    sum_after_max+=after_max[i]
print(f"Сума елементів розташованих після максимального: {sum_after_max}")







