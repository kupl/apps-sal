def vowel_indices(n):
    return [i + 1 for (i, j) in enumerate(n) if j.lower() in 'aeiouy']
