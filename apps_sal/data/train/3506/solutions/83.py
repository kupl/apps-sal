def vowel_indices(word):
    return [p for (p, c) in enumerate(word.lower(), 1) if c in 'aeiouy']
