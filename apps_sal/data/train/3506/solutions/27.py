def vowel_indices(word):
    retVal = []
    vow = ['a', 'e', 'i', 'o', 'u', 'y']
    word = word.lower()
    i = 1
    for letter in word:
        if letter in vow:
            retVal.append(i)
        i += 1
    return retVal
