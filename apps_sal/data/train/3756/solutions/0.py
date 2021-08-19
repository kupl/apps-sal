import math


def goldbach_partitions(n):

    def is_prime(x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    if n % 2:
        return []
    ret = []
    for first in range(2, n // 2 + 1):
        if is_prime(first):
            second = n - first
            if is_prime(second):
                ret.append('%d+%d' % (first, second))
    return ret
