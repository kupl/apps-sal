def reverse_words(text):
    textArray = text.split(" ")
    reversedArray = []
    for word in textArray:
        reversedWord = ''
        for letter in word:
            reversedWord = letter + reversedWord
        reversedArray.append(reversedWord)

    return " ".join(reversedArray)
