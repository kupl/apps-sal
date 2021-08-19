def get_real_floor(n):
    print(n)
    if n == 0:
        return 0
    if n < 13 and n > 0:
        return n - 1
    elif n < 0:
        return n
    else:
        return n - 2
