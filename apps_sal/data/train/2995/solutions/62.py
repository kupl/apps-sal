from math import floor


def sum_mul(n, m):
    print([n, m], flush=True)
    if n > 0 and m > 0:
        i = 1
        sum = 0
        while i * n < m:
            sum += i * n
            i += 1
        return sum
    else:
        return 'INVALID'
