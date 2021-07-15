def vowel_indices(word):
    return [(index+1) for index, ele in enumerate(word.lower()) if ele in 'aeiouy']
