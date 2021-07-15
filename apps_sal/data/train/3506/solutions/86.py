def vowel_indices(word):
    l = []
    for num in range(len(word)):
        if word[num] in "aeiouyAEIOUY":
            l.append(num + 1)
    return l
