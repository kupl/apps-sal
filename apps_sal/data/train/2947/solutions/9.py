def rounding(n, m):
    floored = n // m * m
    diff = n - floored
    return floored if 2 * diff < m else floored + m if 2 * diff > m else n
