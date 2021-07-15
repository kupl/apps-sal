def sort_number(a):
    a.sort()
    return a[:-1]+[2] if set(a) == {1} else [] if len(a) == 0 else [1] if len(a) == 0 else [1] + a[:-1]
