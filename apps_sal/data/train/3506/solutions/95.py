def vowel_indices(word):
    return [i + 1 for (i, x) in enumerate(list(word)) if x in 'aeiouyAEIOUY']
