def array_diff(a, b):
    for n in b:
        while(n in a):
            a.remove(n)
    return a
