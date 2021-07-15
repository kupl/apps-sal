def reverse_number(n):
    return min(1, max(-1, n)) * int(str(abs(n))[::-1])
