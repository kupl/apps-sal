def vowel_indices(word):
  return [i + 1 for (i, x) in enumerate(word.lower()) if x in 'aeiouy']
