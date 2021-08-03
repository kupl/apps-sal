from itertools import*
def transpose_two_strings(a): return '\n'.join(map(' '.join, zip_longest(*a, fillvalue=' ')))
