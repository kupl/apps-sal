def n_closestPairs_tonum(n, k):
    found = []
    for number in range(n - 1, 1, -1):
        (i, limit) = (1, int(number ** 0.5))
        while i <= limit and len(found) < k:
            sq = i * i
            diff = number - sq
            sq1 = (number + diff) ** 0.5
            if sq1.is_integer() and diff:
                found.append([number, diff])
            i += 1
        if len(found) == k:
            break
    return found
