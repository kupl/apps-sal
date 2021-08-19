import re
from operator import add, sub, mul, truediv
letter_re = re.compile('[a-z]')
operations = [add, sub, mul, truediv]


def letter(s):
    return letter_re.search(s).group(0)


def number(s):
    return int(letter_re.sub('', s))


def do_math(s):
    parts = s.split(' ')
    parts.sort(key=letter)
    numbers = [number(p) for p in parts]
    for i in range(1, len(numbers)):
        operation = operations[(i - 1) % 4]
        numbers[0] = operation(numbers[0], numbers[i])
    return round(numbers[0])
