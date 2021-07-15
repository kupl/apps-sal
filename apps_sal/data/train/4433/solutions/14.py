from operator import and_, or_, xor
from functools import reduce

logical_calc = lambda xs, op: reduce({ 'AND': and_, 'OR': or_, 'XOR': xor }.get(op), xs)
