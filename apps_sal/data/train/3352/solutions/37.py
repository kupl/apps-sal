def find_longest(arr):
    mn = ln = -1
    for n in arr:
        l = len(str(n))
        if l > ln:
            (mn, ln) = (n, l)
    return mn
