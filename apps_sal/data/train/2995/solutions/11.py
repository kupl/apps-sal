xrange = range
def sum_mul(n, m):
    if m <= 0 or n <= 0:
        return 'INVALID'
    return sum(x for x in range(m) if x % n == 0)
