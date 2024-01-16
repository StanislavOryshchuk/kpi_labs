myfile = open('input.txt', 'r')
text = myfile.read().split(" ")
print(text)

def has_special_letters(test_str):
    for el in range(len(test_str) - 1):
        if test_str[el] == test_str[el + 1]:
            return True
    return False

special_words = []

for i in range(len(text)):
    word = text[i]
    test_word = has_special_letters(word)
    if test_word:
        special_words.append(word)
print(special_words)


result = []
for w in text:
    if w.lower() in [s.lower() for s in special_words]:
        result.append(w.swapcase())
    else:
        result.append(w)

print(result)
output = open('output.txt', 'w')
output.write(str(result))


