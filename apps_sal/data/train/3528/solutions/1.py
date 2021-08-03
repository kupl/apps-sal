def compound_array(a, b):
    x = min(map(len, (a, b)))
    return sum(map(list, zip(a, b)), []) + a[x:] + b[x:]
