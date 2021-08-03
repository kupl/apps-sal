from string import ascii_uppercase
from functools import reduce

val = {c: i + 1 for i, c in enumerate(ascii_uppercase)}
def add(x, y): return 26 * x + y


def title_to_number(title):
    return reduce(add, map(val.get, title))
