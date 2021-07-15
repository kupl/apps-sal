def choose_best_sum(t, k, ls):
    a = len(ls)
    maxdist = None
    possibilities = [bin(x)[2:].zfill(a) for x in range(2 ** a) if bin(x).count('1') == k]
    for i in possibilities:
        dist = sum([int(i[x]) * ls[x] for x in range(len(i))])
        if dist == t:
            return t
        if dist < t:
            maxdist = max(dist, maxdist)
    return maxdist
