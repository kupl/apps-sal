def reverse_words(text):
    words = text.split(' ')
    newWords = [word[::-1] for word in words]
    print(newWords)
    newSentence = ' '.join(newWords)
    return newSentence
