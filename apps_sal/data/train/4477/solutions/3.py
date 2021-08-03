def reverse_number(n):
    return 0 if n == 0 else n / abs(n) * int(str(abs(n))[::-1])
