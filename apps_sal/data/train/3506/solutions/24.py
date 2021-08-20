def vowel_indices(w):
    return [i + 1 for (i, k) in enumerate(w) if k.lower() in 'aeiouy']
