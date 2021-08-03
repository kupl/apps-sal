def reverse_number(n):
    if n == 0:
        return 0
    s = int(str(abs(n))[::-1])
    return n / abs(n) * s
