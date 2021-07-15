def reverse_number(n):
    return int(str(abs(n))[::-1]) if n>-1 else -int(str(abs(n))[::-1])
