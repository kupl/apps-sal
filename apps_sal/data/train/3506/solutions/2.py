def vowel_indices(word):
    return [index for index, value in enumerate(word.lower(), 1) if value in 'aeyuio']
