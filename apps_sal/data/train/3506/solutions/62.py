def vowel_indices(word):
    return [i for i, ch in enumerate(word.lower(), 1) if ch in 'aeiouy']
