def array_diff(a, b):
    for i in range(len(b)):
        while b[i] in a:
            a.remove(b[i])
    return a
