def reverse_number(n):
    return int(str(abs(n))[::-1]) * (1 - 2 * (n < 0))
