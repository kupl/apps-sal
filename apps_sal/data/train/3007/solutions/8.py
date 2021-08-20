from numpy import roots


def consecutive_sum(num):
    return sum((num % i == (i >> 1) * (i & 1 ^ 1) for i in range(1, int(roots([1 / 2, 1 / 2, -num])[1] + 1))))
