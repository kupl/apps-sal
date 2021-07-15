def reverse_number(n):
    return int(str(n).replace('-','')[::-1]) * (-1 if n < 0 else 1)
