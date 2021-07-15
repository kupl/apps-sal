def vowel_indices(word: str):
    i = []
    word = word.lower()
    word = list(word)
    for l in 'aeiouy':
        while l in word:
            i.append(word.index(l) + 1)
            word[i[-1]-1] = ' '
    return sorted(i)
