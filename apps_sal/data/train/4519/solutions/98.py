def max_number(n):
    a = list(str(n))
    a.sort()
    a.reverse()
    b = ("").join(a)
    return int(b)
