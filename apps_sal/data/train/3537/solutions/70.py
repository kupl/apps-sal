def is_even(n):
    if isinstance(n, int):
        if abs(n) % 2 == 0:
            return True
    return False
