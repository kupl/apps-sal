from functools import reduce


def find_part_max_prod(n):
    partitions = []
    for k in range(1, n + 1):
        part = [n // k + 1] * (n % k) + [n // k] * (k - n % k)
        partitions.append([reduce(int.__mul__, part), part])
    m = max(partitions)[0]
    return [j for (i, j) in partitions if i == m] + [m]
