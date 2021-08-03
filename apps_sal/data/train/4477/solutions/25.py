def reverse_number(n):
    return n // abs(n) * int(str(abs(n))[::-1]) if n != 0 else 0
