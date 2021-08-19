def list_squared(m, n):
    out = []
    for i in range(m, n + 1):
        possibles = set([x for x in range(1, int(i ** 0.5) + 1) if i % x == 0])
        possibles.update([i / x for x in possibles])
        val = sum((x ** 2 for x in possibles))
        if int(val ** 0.5) ** 2 == val:
            out.append([i, val])
    return out
