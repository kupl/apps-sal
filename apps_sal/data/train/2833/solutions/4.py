def sect_sort(a, b=0, c=0):
    c = len(a) if not c else b + c
    return a[:b] + sorted(a[b:c]) + a[c:]
