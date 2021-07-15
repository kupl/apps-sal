def to_freud(sentence):
    return ' '.join(__import__('itertools').repeat('sex', len(sentence.split())))
