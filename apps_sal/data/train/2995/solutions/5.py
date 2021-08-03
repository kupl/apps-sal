def sum_range(end, divisor=None):
    if divisor:
        return int(sum_range(end // divisor)) * divisor
    return end * (end + 1) / 2


def sum_mul(n, m):
    return sum_range(m - 1, divisor=n) if n > 0 and m > 0 else 'INVALID'
