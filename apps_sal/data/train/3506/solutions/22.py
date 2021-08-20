def vowel_indices(word):
    return [i + 1 for (i, lett) in list(enumerate(word.lower())) if lett in 'aeiouy']
