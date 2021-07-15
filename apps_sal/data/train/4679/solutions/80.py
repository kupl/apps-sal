def to_freud(sentence):
  return ' '.join('sex' for i in range(1, len(sentence.split(' '))+1))
