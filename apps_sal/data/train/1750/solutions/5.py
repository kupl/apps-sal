def mystery(n):
    return n ^ (n >> 1)

def mystery_inv(n):
    res = 0
    while n > 0:
        res ^= n
        n >>= 1
    return res

def name_of_mystery():
    return 'Gray code'
