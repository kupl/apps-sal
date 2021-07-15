def to_freud(sentence):
    l = sentence.split()
    s = ['sex'] * len(l)
    return ' '.join(s)
