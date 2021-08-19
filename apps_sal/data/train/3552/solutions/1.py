def update_score(score, trump, alone, tricks):
    (ts, sc) = (tricks.count(trump), score[:])
    if ts <= 2:
        sc[trump - 1 ^ 1] += 2
    else:
        sc[trump - 1] += [[1, 2][not alone and ts == 5], 4][alone and ts == 5]
    return sc
