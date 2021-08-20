def to_freud(sentence):
    return ' '.join((word.replace(word, 'sex') for word in sentence.split(' ')))
