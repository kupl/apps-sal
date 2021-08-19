from functools import partial
from re import compile
reverse = partial(compile('(.)\\1+').sub, lambda s: s.group().swapcase())
