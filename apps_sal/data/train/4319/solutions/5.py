ONE_ZERO = 'abdegopq069DOPQR'
TWO_ZERO = '%&B8'
def countzero(string):
    string = string.replace('()', '0')
    return sum(1 if c in ONE_ZERO else 2 if c in TWO_ZERO else 0 for c in string)
