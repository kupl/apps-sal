import re


def count_letters_and_digits(s):
    return len(re.sub('[\\W_]', '', s))
