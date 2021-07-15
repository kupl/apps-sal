def to_freud(sentence):
    repeats = len(sentence.split(' '))
    return ' '.join(['sex'] * repeats)
