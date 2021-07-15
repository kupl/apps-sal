def reverse_number(n):
    neg = 0
    if abs(n) != n:
        n = -n
        neg = 1
    n = int(str(n)[::-1])
    return -n if neg == 1 else n
