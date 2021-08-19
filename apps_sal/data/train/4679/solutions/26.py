def to_freud(sentence):
    return ' '.join(('sex' for i in range(len(sentence.split(' ')))))
