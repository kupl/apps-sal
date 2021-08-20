def to_freud(sentence):
    a = sentence.split(' ')
    b = ''
    for i in a:
        if not b:
            b += 'sex '
        else:
            b += 'sex '
    if b[-1] == ' ':
        return b[:-1]
    else:
        return b
