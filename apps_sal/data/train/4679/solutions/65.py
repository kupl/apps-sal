def to_freud(sentence):
    list = sentence.split(' ')
    return ' '.join(['sex' for i in range(len(list))])
