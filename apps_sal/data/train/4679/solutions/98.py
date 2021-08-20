def to_freud(sentence):
    return ' '.join(('sex' for x in range(len(sentence.split()))))
