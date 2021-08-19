def to_freud(sentence):
    a = sentence.split(' ')
    for i in range(len(a)):
        a[i] = 'sex'
    return ' '.join(a)
