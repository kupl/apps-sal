def or_arrays(a, b, d=0):
    return [(a[i] if i<len(a) else d)|(b[i] if i<len(b) else d) for i in range(max(len(a), len(b)))]
