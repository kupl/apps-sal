mask = 2863311530


def int_to_negabinary(i):
    return '{0:b}'.format(mask + i ^ mask)


def negabinary_to_int(s):
    return (int(s, 2) ^ mask) - mask
