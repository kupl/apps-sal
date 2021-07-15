def histogram(lst, w):
    lst = [n // w for n in lst]
    m = max(lst, default=-1) + 1
    return [lst.count(n) for n in range(m)]
