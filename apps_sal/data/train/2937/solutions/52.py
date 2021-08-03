def between(a, b):
    x = []
    while b >= a:
        x.append(a)
        a = a + 1
    return x
