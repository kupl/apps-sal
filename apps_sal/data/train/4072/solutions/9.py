def permutation_position(perm):
    a = list(perm)[::-1]
    res = 0
    k = 0
    for el in a:
        res += (ord(el) - 97) * 26 ** k
        k += 1
    return res + 1
