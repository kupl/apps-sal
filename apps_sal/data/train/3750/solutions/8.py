import re


def count_letters_and_digits(s):
    return len(re.sub(r'[\W_]', '', s))
