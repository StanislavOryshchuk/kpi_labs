string = input()

words = string.split()
lent = len(words)

print("Ви ввели", words)
#=========================================================================#
balanced_words = []
for slovo in words:
    for j in range(len(slovo)):
        letter = slovo[j]
        golosni = 0
        prugolosni = 0
        for letter in slovo:
            if letter.lower() in 'аоуеіияюїє':
                golosni += 1
            else:
                prugolosni += 1
    if golosni == prugolosni:
        balanced_words.append(slovo)
    print( slovo, " || голосні", golosni, "приголосні", prugolosni)
print("Кількість слів, у яких одинаково голосних і приголосних:   ", len(balanced_words), ":", balanced_words)

print("---------- далi")
if input()=="б":
    len_of_words = []
    for i in range(lent):
        slovo = words[i]
        lenghta = len(slovo)
        len_of_words.append(lenghta)
    print("Довжина слів", len_of_words)
    max_index = max(len_of_words)
    wer = len_of_words.index(max_index)
    slovo_max = words[wer]

print("Найдовше слово", slovo_max)

input("далі")

if input()=="в":
    words_for_removed = []
    for slovo in words:
        check_palindrom = 0
        palind = ''
        for i in range(len(slovo)):
            if slovo[i] == slovo[len(slovo) - i - 1]:
                check_palindrom = check_palindrom + 1
        if check_palindrom >= float(len(slovo) / 2):
            palind = " є паліндромом"
        print(slovo, palind)

        if check_palindrom >= float(len(slovo) / 2):
            words_for_removed.append(slovo)

    print("Слова-паліндром, які мають бути видалені: ", words_for_removed)
    for wer in words:
        if wer in words_for_removed:
            words.remove(wer)
    print("Очищений список", words)


#Піп Пилип купив собі шалаш
""" Степан розповів що піп купив собі шалаш кан """

