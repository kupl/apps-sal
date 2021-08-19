def vowel_indices(word):
    word = word.lower()
    word = list(word)
    vowel = ['a', 'e', 'i', 'o', 'u', 'y']
    result = []
    for (i, j) in enumerate(word):
        if j in vowel:
            result.append(i + 1)
    return result
