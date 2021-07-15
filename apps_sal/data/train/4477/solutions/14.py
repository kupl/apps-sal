def reverse_number(n):
    return int(str(n)[::-1]) if n > 0 else -int(str(abs(n))[::-1])
