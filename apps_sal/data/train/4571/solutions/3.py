from itertools import count
from math import log

def decompose(num):
    result = []
    for x in count(2):
        if num < x*x:
            return [result, num]
        result.append(int(log(num, x)))
        num -= x**result[-1]
