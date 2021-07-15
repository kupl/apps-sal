xrange = range

def sum_mul(n, m):
    if m <= 0 or n <= 0:
        return "INVALID"
    k = (m - 1) // n
    return (k + 1) * k // 2 * n
