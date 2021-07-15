def reverse_number(n):
    if n < 0:
        return 0 - int(str(n)[::-1][:-1])
    return int(str(n)[::-1])
