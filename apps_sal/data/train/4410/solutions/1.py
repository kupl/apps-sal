def count_sixes(n):
    return len(str(1 << n - n % 2)) - 1
