
file = open("wordle_words.txt", "r")
wordle_list = []

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
result = {}
for word in file:
    wordle_list.append(word.replace("\n",""))

test_list = wordle_list[:10]
print(test_list)
for letter in alphabet:
    result[letter] = 0
    for word in wordle_list:
        for l in word:
            if letter == l:
                result[letter] += 1

print(result)



