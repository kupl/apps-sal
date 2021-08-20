def multiply(n):
    a = str(n)
    l = []
    d = 5
    for x in a:
        l.append(x)
    if n > 0:
        for x in range(0, len(l)):
            n = n * 5
    if n < 0:
        for x in range(0, len(l) - 1):
            n = n * 5
    return n
