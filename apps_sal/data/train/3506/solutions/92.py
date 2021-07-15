def vowel_indices(word):
  vowel = "aeiouyAEIOUY"

  return [x + 1 for x in range(len(word)) if word[x] in vowel]
