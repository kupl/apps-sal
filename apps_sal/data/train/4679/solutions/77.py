def to_freud(sentence):
  sentence = ['sex' for word in sentence.split(' ')]
  return ' '.join(sentence)
