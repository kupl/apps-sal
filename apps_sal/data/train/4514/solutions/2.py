def int_to_negabinary(i):
    return '{:b}'.format(2863311530 + i ^ 2863311530)


def negabinary_to_int(n):
    return (int(n, 2) ^ 2863311530) - 2863311530
