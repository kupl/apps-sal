def reverse_number(n):
    sign = -1 if n < 0 else 1
    return sign * int(str(n).replace('-', '')[::-1])
