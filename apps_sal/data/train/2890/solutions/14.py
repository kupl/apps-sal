def multiples(m, n):
    l = []
    current = 0
    for i in range(1, m + 1):
        if i <= m:
            current = i * n
            l.append(current)
    return l
