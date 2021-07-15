def tidyNumber(n):
    a = list(str(n))
    a.sort()
    b = ("").join(a)
    c = int(b)
    if c == n:
        return True
    else:
        return False
