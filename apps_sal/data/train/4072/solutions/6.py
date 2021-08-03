permutation_position = lambda p, a=__import__('string').printable: int(p.translate(p.maketrans(a[10:36], a[:26])), 26) + 1
