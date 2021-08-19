from re import findall
from itertools import cycle


def do_math(s):
    numbers = [''.join(findall('\\d+', num)) for num in sorted(s.split(), key=lambda x: max(x))]
    res = numbers[0]
    for (i, operation) in zip(numbers[1:], cycle('+-*/')):
        res = eval(f'{res} {operation} {i}')
    return round(float(res))
