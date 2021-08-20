def vowel_indices(word):
    return [i for (i, c) in enumerate(word.lower(), 1) if c in 'aeiouy']
