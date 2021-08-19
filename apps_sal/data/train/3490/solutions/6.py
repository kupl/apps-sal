def array_manip(a):
    return [min([m for m in a[i + 1:] if m > n] or [-1]) for (i, n) in enumerate(a)]
