def sc_perm_comb(n):
    return sum({int(''.join(p)) for r in range(len(str(n))) for p in __import__('itertools').permutations(str(n), r + 1)})
