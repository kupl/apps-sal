def permutations(string):
    from itertools import permutations
    a=[''.join(x) for x in permutations(string)]
    return list(set(a))
