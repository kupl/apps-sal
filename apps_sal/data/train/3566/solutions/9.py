def find_missing(a, b):
    for x in b:
        a.remove(x)

    return a[0]
