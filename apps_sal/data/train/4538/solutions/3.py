def reverse_fun(n, first=False):
    return "" if len(n) < 1 else n[0] + reverse_fun(n[1:]) if first else n[-1] + reverse_fun(n[:-1], True)
