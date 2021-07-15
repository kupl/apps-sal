def get_real_floor(n: int) -> int:
    return 0 if n == 1 or n == 0 else n - 2 if n > 13 else n if n < 0 else n - 1
