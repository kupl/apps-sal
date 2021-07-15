def to_freud(sentence):
    return ' '.join(['sex' if len(sentence) > 1 else '' for i in sentence.split()])
