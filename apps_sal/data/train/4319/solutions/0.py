def countzero(s):
    return sum((1 if c in 'abdegopq069DOPQR' else 2 if c in '%&B8' else 0 for c in s.replace('()', '0')))
