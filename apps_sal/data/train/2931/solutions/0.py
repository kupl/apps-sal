def count_cows(n):
    if not isinstance(n, int):
        return None
    return 1 if n < 3 else count_cows(n-1) + count_cows(n-3)
