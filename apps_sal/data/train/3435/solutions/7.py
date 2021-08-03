from functools import partial
from numpy import sign
from re import compile

remove = partial(compile(r".?\*+.?").sub, "")
memo = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': -4, 'q': -3, 'd': -2, 'z': -1}
result = ("Let's fight again!", "Left side wins!", "Right side wins!")
def value(c): return memo.get(c, 0)


def alphabet_war(fight):
    return result[sign(sum(map(value, remove(fight))))]
