from itertools import product

def coin(n):
    return [''.join(xs) for xs in product('HT', repeat=n)]
