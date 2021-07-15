def odd_count(n: int) -> int:
    """This functions returns the number of positive odd numbers below 'n'."""
    if n <= 0:
        return 0
    return n // 2
