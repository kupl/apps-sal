def vowel_indices(word):
    vowels = list()
    test = 'aeiouyAEIOUY'
    for i in range(0, len(word)):
        if test.find(word[i]) >= 0:
            vowels.append(i + 1)
    return vowels
