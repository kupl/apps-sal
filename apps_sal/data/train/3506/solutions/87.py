def vowel_indices(word):
    res = []
    vowels = ['a', 'o', 'u', 'i', 'e', 'y']
    for i in range(len(word)):
        if word[i].lower() in vowels:
            res.append(i + 1)
    return res
