def int_to_negabinary(i):
    return bin(i + 2863311530 ^ 2863311530)[2:]


def negabinary_to_int(s):
    return sum((int(d) * (-2) ** i for (i, d) in enumerate(s[::-1])))
