import re


def solve(s):
    list_numbers = re.sub("[^0-9]", " 0 ", s)
    return max([int(i) for i in list_numbers.split()])
