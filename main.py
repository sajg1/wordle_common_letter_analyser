
file = open("wordle_words.txt", "r")
wordle_list = []

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
letter_totals = []
for word in file:
    wordle_list.append(word.replace("\n",""))

test_list = wordle_list[:10]
print(test_list)
for letter in alphabet:
    result = {"letter": letter,"total": 0}
    for word in wordle_list:
        for char in word:
            if letter == char:
                result["total"] += 1
    letter_totals.append(result)

sorted_list = sorted(letter_totals, key=lambda d: d['total'], reverse=True)
print(sorted_list)




