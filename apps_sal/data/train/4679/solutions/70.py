def to_freud(sentence):
    count = len([i for i in sentence.split()])
    return ' '.join(['sex' for i in range(0, count)])
