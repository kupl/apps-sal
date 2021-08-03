from itertools import permutations


def find_mult_3(s):
    x = []
    for i in range(1, len(str(s)) + 1):
        x += [int(''.join(p)) for p in list(set(permutations(str(s), i))) if not int(''.join(p)) % 3 and p[0] != '0']
    return [len(x), max(x)]
