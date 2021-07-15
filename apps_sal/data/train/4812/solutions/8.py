def nth_floyd(n):
    i = 0
    j = 0
    while n > j:
        i += 1
        j += i
    return i
