def multiply(n):
    t, flag = (n, False) if n > 0 else (abs(n), True)
    res = n * (5**len(str(t)))
    return res
