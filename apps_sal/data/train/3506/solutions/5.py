def vowel_indices(word):
    return [i + 1 for (i, v) in enumerate(word) if v.lower() in 'aeiouy']
