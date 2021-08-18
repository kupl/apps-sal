def to_freud(sentence):
    a = ''
    for i in range(len(sentence.split())):
        a += 'sex '
    return a[:-1]
