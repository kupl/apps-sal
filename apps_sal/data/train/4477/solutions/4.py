def reverse_number(n):
    return int(str(abs(n))[::-1]) * (-1) ** (n < 0)
