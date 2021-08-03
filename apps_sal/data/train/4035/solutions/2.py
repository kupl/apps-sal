def substring_test(a, b):
    if len(a) > len(b):
        a, b = b, a
    a, b = a.lower(), b.lower()
    return any(a[i:i + 2] in b for i in range(len(a) - 1))
