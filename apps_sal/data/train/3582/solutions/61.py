def is_digit(n):
    return isinstance(n, str) and len(n) == 1 and (0 <= ord(n) - ord('0') <= 9)
