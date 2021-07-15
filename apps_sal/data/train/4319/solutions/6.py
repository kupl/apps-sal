zeroes = {}
for c in 'abdegopq069DOPQR':
    zeroes[c] = 1
for c in '%&B8':
    zeroes[c] = 2

def countzero(string):
    string = string.replace('()', '0')
    return sum(map(lambda c: zeroes.get(c, 0), string))
