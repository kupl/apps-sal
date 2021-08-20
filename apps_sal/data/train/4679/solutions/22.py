def to_freud(sentence):
    wordCount = len(sentence.split(' '))
    list = ['sex'] * wordCount
    return ' '.join(list)
