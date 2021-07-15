from functools import reduce
from operator import xor, or_

disjunction = lambda a, b: reduce(xor if b else or_, a)
