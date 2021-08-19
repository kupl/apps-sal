def is_substitution_cipher(a, b):
    (d1, d2) = ({}, {})
    for (x, y) in zip(a, b):
        if x in d1 and d1[x] != y or (y in d2 and d2[y] != x):
            return 0
        d1[x] = y
        d2[y] = x
    return 1
