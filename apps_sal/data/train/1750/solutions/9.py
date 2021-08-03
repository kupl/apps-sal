def mystery(n):
    return n ^ (n >> 1)


def mystery_inv(n):
    b = 0  # next bit to append to result
    p = 1 << (n).bit_length()  # power of 2 greater than n
    result = 0
    while p > 1:
        p >>= 1
        if n & p != 0:
            b = 1 - b  # flip bit when a 1 is in corresponding bit position in n
        result = (result << 1) + b
    return result


def name_of_mystery():
    return 'Gray code'
