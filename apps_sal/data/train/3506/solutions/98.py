def vowel_indices(word):
    return [i+1  for i, a in enumerate(word.lower()) if a in (list('aeiouy'))]
