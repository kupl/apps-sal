def jumping(a, n):
    i = 0
    while i < len(a):
        temp = a[i]
        a[i] += 1 if a[i] < n else -1
        i += temp
    return a.count(n)
