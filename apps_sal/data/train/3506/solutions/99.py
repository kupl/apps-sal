def vowel_indices(word):
    return [c+1 for c,i in enumerate(word.lower()) if i in 'aeiouy']
