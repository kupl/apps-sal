def nth_floyd(n):
    s = i = 0
    while s < n:
        i += 1
        s += i
    return i
