def to_freud(sentence):
    if sentence is not None:
        return ' '.join(map(lambda x: 'sex', sentence.split(' ')))
    return ''
