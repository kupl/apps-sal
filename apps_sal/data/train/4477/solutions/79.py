def reverse_number(n):
    res = int(str(abs(n))[::-1])
    return res if n >= 0 else -res
