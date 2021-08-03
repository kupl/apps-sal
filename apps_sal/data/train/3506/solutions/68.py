
def vowel_indices(word):
    res = []
    for i, char in enumerate(word):
        if char in 'aeiouyAEIOUY':
            res.append(i + 1)
    return res
