def vowel_indices(word):
    return [a + 1 for (a, c) in enumerate(word) if c in 'aeiouyAEIOUY']
