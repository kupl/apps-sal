def vowel_indices(word):
    return [i + 1 for (i, n) in enumerate(word.lower()) if n in ['a', 'e', 'i', 'o', 'u', 'y']]
