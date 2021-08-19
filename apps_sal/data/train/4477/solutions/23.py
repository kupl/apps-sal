def reverse_number(n):
    if n > 0:
        f = int(str(abs(n))[::-1])
    else:
        f = -int(str(abs(n))[::-1])
    return f
