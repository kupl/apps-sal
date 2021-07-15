def to_freud(sentence):
  #your code here
    return ' '.join([ i.replace(i, 'sex') for i in sentence.split(' ')])

