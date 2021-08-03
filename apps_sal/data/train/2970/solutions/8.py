import itertools
import collections


def factorize(n):
    factors = []
    if n <= 1:
        return [n]
    for i in range(2, n + 1):
        if n <= 1:
            break
        while n % i == 0:
            factors.append(i)
            n /= i
    return factors


def prod_int_part(n):
    fac = factorize(n)
    x = len(fac) - 1
    for i in range(x):
        fac.append("/")
    perms = set(list(itertools.permutations(fac)))
    all_perm_factors = []
    for perm in perms:
        perm_factors = []
        prod = 1
        for i in range(len(perm)):
            if perm[i] != "/":
                prod *= perm[i]
            elif perm[i] == "/":
                perm_factors.append(prod)
                prod = 1
        perm_factors.append(prod)
        perm_counter = collections.Counter(x for x in perm_factors if x != 1)
        if not perm_counter in all_perm_factors:
            all_perm_factors.append(perm_counter)
    l = factorize(n)
    if len(l) == 1:
        del(l[0])
    return [len(all_perm_factors) - 1, l]
