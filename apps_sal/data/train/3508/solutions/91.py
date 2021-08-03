from math import trunc


def halving_sum(n):
    result = divided = n
    divisor = 1
    while divided > 1:
        divisor *= 2
        divided = n // divisor
        result += divided
    return result
