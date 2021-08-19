import re


def filter_numbers(s):
    return re.sub('[0-9]', '', s)
