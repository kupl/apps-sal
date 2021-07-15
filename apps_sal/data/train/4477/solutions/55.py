def reverse_number(n):
    return int(str(abs(n))[::-1]) * (n < 0 and -1 or 1)
