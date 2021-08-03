def divisible_count(x, y, k):
    return (y // k) - (x // k) + bool(x % k == 0)
