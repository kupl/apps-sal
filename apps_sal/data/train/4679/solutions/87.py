def to_freud(sentence):
    return "" if not sentence else ' '.join('sex' for elem in sentence.split() if elem.isalpha() or "'" in elem)
  #your code here

