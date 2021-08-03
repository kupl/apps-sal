from fractions import gcd
from sys import maxsize


def an(length):
    current = 7
    for index in range(length):
        yield current
        current += gcd(index + 2, current)


def gn(length):
    previous = False
    for current in an(length):
        if previous:
            yield current - previous
        else:
            yield 1
        previous = current


def pn(length):
    seen = set()
    count = 0
    for current in gn(maxsize):
        if current != 1 and current not in seen:
            seen.add(current)
            count += 1
            yield current
        if count == length:
            break


def max_pn(length):
    return max(pn(length))


def an_over(length):
    count = 0
    for i, (a, g) in enumerate(zip(an(maxsize), gn(maxsize))):
        if g != 1:
            count += 1
            yield a / (i + 1)
        if count == length:
            break


def an_over_average(length):
    return sum(an_over(length)) / length


def count_ones(length):
    count = 0
    for x in gn(length):
        if x == 1:
            count += 1
    return count
