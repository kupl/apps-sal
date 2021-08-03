from math import sqrt


def non_unique_partitions(n, floor=2):
    count = 0
    for i in range(floor, int(sqrt(n)) + 1):
        if n % i == 0:
            count += 1 + non_unique_partitions(n // i, i)
    return count


def factorize_without_n(n):
    fac = []
    for i in range(2, n):
        while n % i == 0:
            fac.append(i)
            n = n // i
    return fac


def prod_int_part(n):
    return [non_unique_partitions(n), factorize_without_n(n)]
