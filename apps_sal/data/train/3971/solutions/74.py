def tidyNumber(n):
    x = list(str(n))
    return True if x == sorted(x) else False
