def vowel_indices(word):
    r = []
    for i, c in enumerate(word):
        if c in 'aeiouyAEIOUY':
            r.append(i + 1)
    return r
