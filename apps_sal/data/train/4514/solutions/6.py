def int_to_negabinary(i):
    mask = 187649984473770
    return bin(i + mask ^ mask)[2:]


def negabinary_to_int(s):
    mask = 187649984473770
    return (int(s, 2) ^ mask) - mask
