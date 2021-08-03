def divisible_count(x, y, k):
    d = x % k
    if x >= 0:
        return (d == 0) + (y - x + d) // k
