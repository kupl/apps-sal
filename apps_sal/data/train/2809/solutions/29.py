def digitize(n):
    a = []
    while n != 0:
        a.append(n % 10)
        n = n // 10
    return a
