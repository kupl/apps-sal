def reverse_words(str):
  return ' '.join(map(lambda x: x[::-1], str.split(' ')))
