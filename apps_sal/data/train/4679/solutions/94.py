def to_freud(sentence):
    # your code here
    a = ''
    for i in range(len(sentence.split())):
        a += 'sex '
    return a[:-1]
