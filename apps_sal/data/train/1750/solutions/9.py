def mystery(n):
    return n ^ n >> 1


def mystery_inv(n):
    b = 0
    p = 1 << n.bit_length()
    result = 0
    while p > 1:
        p >>= 1
        if n & p != 0:
            b = 1 - b
        result = (result << 1) + b
    return result


def name_of_mystery():
    return 'Gray code'
