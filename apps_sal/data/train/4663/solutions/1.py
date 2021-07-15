def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
