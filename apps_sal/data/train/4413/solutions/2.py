import re


def split_odd_and_even(n):
    return [int(x) for x in re.findall('([2468]+|[13579]+)', str(n))]
