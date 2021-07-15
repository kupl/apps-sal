import itertools

def decode(code, key):
    return ''.join(chr(96+i-int(j)) for i, j in zip(code, itertools.cycle(str(key))))

