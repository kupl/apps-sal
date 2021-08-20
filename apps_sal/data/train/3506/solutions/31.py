def vowel_indices(word):
    word = word.lower()
    res = []
    for i in range(len(word)):
        if word[i] in 'aeiouy':
            res.append(i + 1)
    return res
