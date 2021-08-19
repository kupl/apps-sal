def vowel_indices(word):
    return [word.find(c, i) + 1 for (i, c) in enumerate(word) if c.lower() in 'aeiouy']
