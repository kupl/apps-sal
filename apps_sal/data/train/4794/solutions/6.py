def comfortable_numbers(l, r):
    pairs = set()
    for a in range(l, r + 1):
        s = sum((int(d) for d in str(a)))
        pairs |= set(((a, x) for x in range(max(l, a - s), min(r, a + s) + 1) if x != a))
    return sum(((y, x) in pairs for (x, y) in pairs)) // 2
