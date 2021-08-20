from itertools import permutations


def sc_perm_comb(num):
    s = str(num)
    return sum({int(''.join(p)) for (c, _) in enumerate(s, 1) for p in permutations(s, c)})
