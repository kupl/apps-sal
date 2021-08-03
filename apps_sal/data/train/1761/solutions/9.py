import math


def find(n):
    level = []
    sum2, result, i = 0, 0, 0
    rem = 3
    current = 2
    while sum2 <= n:
        sum2 += (i + 1) * current
        result += current
        i += 1
        rem -= 1
        level.append(current)
        if rem == 0:
            rem = level[current]
            current += 1
    return result - math.ceil((sum2 - n) / (i))
