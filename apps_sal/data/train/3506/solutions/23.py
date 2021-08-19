def vowel_indices(word):
    return [i + 1 for (i, z) in enumerate(word) if z in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']]
