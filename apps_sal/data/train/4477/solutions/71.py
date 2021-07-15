def reverse_number(n):
    return int(str(n)[::-1].replace("-", "")) * n / abs(n) if n != 0 else 0
