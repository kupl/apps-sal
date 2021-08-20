def n_closestPairs_tonum(num, k):
    result = []
    for m in range(num - 1, 1, -1):
        for q in range(1, int(m ** 0.5)):
            n = m - q ** 2
            if int((m + n) ** 0.5) ** 2 == m + n:
                result.append([m, n])
                if len(result) == k:
                    return result
    return result
