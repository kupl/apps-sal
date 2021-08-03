def first_non_consecutive(a):
    i = 0
    n = None
    while i < len(a) - 1:
        if a[i] + 1 != a[i + 1]:
            n = a[i + 1]
            break
        i += 1
    return n
