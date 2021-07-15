def to_freud(sentence):
  if not sentence:
      return ''
      
  return ' '.join(len(sentence.split(' ')) * ['sex'])
