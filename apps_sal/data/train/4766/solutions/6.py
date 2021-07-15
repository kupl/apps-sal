def n_closestPairs_tonum(num, k):
    r = []
    for a in range(int((2 * num - 2) ** 0.5), 1, -1):
        for b in range(min(int((a * a - 1) ** 0.5), int((2 * num - 2 - a * a) ** 0.5)), 0, -1):
            if a % 2 == b % 2:
                r.append([a ** 2 + b ** 2 >> 1, a ** 2 - b ** 2 >> 1])
    return sorted(r, reverse=True)[:k]
