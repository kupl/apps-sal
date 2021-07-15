def vowel_indices(word):
    return [idx for idx, i in enumerate(word, start=1) if i.lower() in 'aeiouy']
