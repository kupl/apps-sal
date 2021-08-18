from math import ceil, log10


def validate_code(code):
    return first_digit(code) in (1, 2, 3)


def first_digit(num):
    num_of_digs = ceil(log10(num))
    amount_of_digs_to_remove = num_of_digs - 1
    return num // 10**(amount_of_digs_to_remove)
