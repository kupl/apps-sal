def monkey_count(n):
    a = []
    while n > 0:
        a.append(n)
        n -= 1
    a.sort()
    return a
