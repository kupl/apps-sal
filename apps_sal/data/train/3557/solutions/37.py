def odd_count(n: int) -> int:
    """Return the number of positive odd numbers below n."""
    if n % 2 == 0:
        odd_count = n / 2
    else:
        odd_count = n // 2
    return odd_count
