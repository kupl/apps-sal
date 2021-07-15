def vowel_indices(word):
    res = []
    for idx, letter in enumerate(word.lower(), 1):
        if letter in 'aeiouy':
            res.append(idx)
    return res
