def int_to_negabinary(i):
    mask = 0xAAAAAAAAAAAA
    return bin((i + mask) ^ mask)[2:]


def negabinary_to_int(s):
    mask = 0xAAAAAAAAAAAA
    return (int(s, 2) ^ mask) - mask
