def max_number(n):
    a = list(str(n))
    a.sort(reverse=True)
    b = "".join(a)
    return int(b)
