def to_freud(sentence):
  sentence = sentence.split()
  return ' '.join(['sex' for i in sentence])
