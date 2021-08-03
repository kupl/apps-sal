def pattern(n):
    p = []
    for i in range(1, n + 1):
        p.append(str(i) * i)
    return "\n".join(p)
