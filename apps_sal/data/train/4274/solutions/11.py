from re import findall
from itertools import cycle


def do_math(s):
    number_letter = [(findall('[A-Za-z]', x)[0], ''.join(findall('\\d+', x))) for x in s.split()]
    numbers = [n for (_, n) in sorted(number_letter, key=lambda x: x[0])]
    res = numbers[0]
    for (i, operation) in zip(numbers[1:], cycle('+-*/')):
        res = eval(f'{res} {operation} {i}')
    return round(float(res))
