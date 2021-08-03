def is_even(n):
    n = abs(n)
    if isinstance(n, float) or n % 2 == 1:
        return False
    else:
        return True
