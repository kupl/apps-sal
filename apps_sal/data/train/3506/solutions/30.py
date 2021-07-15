def vowel_indices(word):
    return [loop + 1 for loop, i in enumerate(word) if i in 'aeiouyAEIOUY']
