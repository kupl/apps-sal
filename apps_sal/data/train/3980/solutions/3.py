from functools import partial
from re import compile

reverse = partial(compile(r"(.)\1+").sub, lambda s: s.group().swapcase())
