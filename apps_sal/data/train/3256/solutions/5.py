def sum_pow_dig_seq(start, n, k):
    cycle, l, h, drop = set(), [], -1, False
    for i in range(k):
        start = sum(int(d)**n for d in str(start))
        if h != -1 and start in cycle:
            break
        if h == -1 and start in cycle:
            cycle, h, l = set(), i, []
        cycle.add(start)
        l.append(start)
    return [h - len(l) + 1, l, len(l), l[(k - i - 1) % len(l)]]
