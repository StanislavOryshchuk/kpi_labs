myfile = open('ATS.txt', 'r')
s_phone = str(input("Введіть номер телефону: "))

if s_phone[0] == "+":
    search_phone = s_phone[0:12]
else:
    search_phone = s_phone

data = myfile.readlines()
result = []

for i in data:
    split_data = i.split()

    if s_phone == "всі":
        print(split_data)

    phone = split_data[0]
    time = int(split_data[1])
    tarif = int(split_data[2])

    if search_phone in phone:
        result.append(phone)
        result.append(time)
        result.append(tarif)
        suma = time*tarif
        result.append(suma)
    else:
        result.append("Номер не знайдено")
        result.append("")
        result.append("")
        result.append("")


if len(result) > 1:
    print("Номер телефону", result[0])

    print("Час розмов, хв", result[1])
    print("Тариф, грн за хв", result[2])
    print("Сума до сплати", result[3])


