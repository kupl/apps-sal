T = str.maketrans('BFPVCGJKQSXZDTLMNR', '111122222222334556')
V = str.maketrans({v: None for v in 'AEIOUY'})


def soundex(name):
    return ' '.join((wordex(w) for w in name.upper().split()))


def wordex(word):
    w = (word[0] + word[1:].replace('W', '').replace('H', '')).translate(T)
    for c in '123456':
        while c + c in w:
            w = w.replace(c + c, c)
    return ((word[0] if w[0].isdigit() else w[0]) + w[1:].translate(V) + '000')[:4]
