def sort_number(a):
    a = sorted(a)
    if a[len(a) - 1] != 1:
        a[len(a) - 1] = 1
    else:
        a[len(a) - 1] = 2
    return sorted(a)
