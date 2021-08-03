def array_madness(a, b):
    sa = 0
    sb = 0
    for i in range(0, len(a)):
        sa += a[i]**2
    for i in range(0, len(b)):
        sb += b[i]**3
    return sa > sb
