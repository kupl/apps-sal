def reverse_words(text):
    finalWord = ' '
    newWord = text.split(' ')
    for word in newWord:
        word = word[::-1]
        finalWord = finalWord + word + ' '
    return finalWord.strip()
