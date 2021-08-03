def vowel_indices(word):
    l = []
    for i in range(len(word)):
        if word[i] in 'aeiouAEIOUyY':
            l.append(i + 1)
    return l
