def vowel_indices(w):
    return [x[0]+1 for x in enumerate(w.lower()) if x[1] in 'aeiouy']
