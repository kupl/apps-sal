def mystery(n):
    return n ^ n >> 1


def mystery_inv(n):
    i = n >> 1
    while i > 0:
        n ^= i
        i >>= 1
    return n


def name_of_mystery():
    return 'Gray code'
