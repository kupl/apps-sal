def to_freud(sentence):
    s1 = sentence.split(' ')
    return ' '.join(['sex'] * len(s1))
