def smash(words):
    newWords = ''
    for letters in words:
        newWords += letters
        if letters != words[-1]:
            newWords += ' '
    return newWords
