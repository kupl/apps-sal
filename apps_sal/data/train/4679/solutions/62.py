def to_freud(sentence):
    x = sentence.split()
    sum = ''
    for y in x:
        sum += 'sex '
    return sum.rstrip(' ')
