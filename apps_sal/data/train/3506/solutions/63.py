def vowel_indices(word):
    res = []
    for i in range(len(word)):
        if word.lower()[i] in 'aeiouy':
            res.append(i + 1)
    return res
