def to_freud(sentence):
    return ' '.join((sentence.count(' ') + 1) * ['sex']) if sentence else ''
