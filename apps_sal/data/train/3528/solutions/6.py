def compound_array(a, b):
    lst = zip(a[:len(b)], b[:len(a)])
    return [item for sublist in lst for item in sublist] + a[len(b):] + b[len(a):]
