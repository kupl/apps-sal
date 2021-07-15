def digitize(n):
    arr = list(str(n))
    rev = []
    for i in arr:
        rev.insert(0, int(i))
    return rev
