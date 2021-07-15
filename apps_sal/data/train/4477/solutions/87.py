def reverse_number(n):
    n = str(n)
    if int(n) < 0:
        return int(n[0] + n[:0:-1])
    else:
        return int(n[::-1])
