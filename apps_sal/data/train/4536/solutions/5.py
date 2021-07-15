def capitals_first(text):
  return ' '.join(sorted(filter(lambda w: w[0].isalpha(), text.split()), key=lambda w: w[0].islower()))
