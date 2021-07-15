def n_closestPairs_tonum(upper_lim, k):
    square_lim = int((2 * upper_lim) ** .5) + 1
    squares = [n*n for n in range(1, square_lim)]
    p, s = [], set(squares)
    for m in range(upper_lim - 1, 1, -1):
        for b in squares:
            if b >= m: break
            if 2*m - b in s:
                p.append([m, m - b])
                if len(p) == k: return p
