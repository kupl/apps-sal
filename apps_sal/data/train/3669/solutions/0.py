from itertools import permutations


def sc_perm_comb(num):
    sNum = str(num)
    return sum({int(''.join(p)) for d in range(1, len(sNum) + 1) for p in permutations(sNum, d)})
