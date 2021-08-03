import re


def is_digit(n):
    return len(str(n)) == 1 and str.isdigit(str(n))
