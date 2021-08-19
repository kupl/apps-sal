def to_freud(sentence):
    return ' '.join([i.replace(i, 'sex') for i in sentence.split(' ')])
