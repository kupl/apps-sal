def reversi_row(a):
    r = ['.'] * 8
    for (p, i) in enumerate(a):
        (cur, opp) = ('*O'[p % 2], '*O'[1 - p % 2])
        r[i] = cur
        for range_ in (range(i - 1, -1, -1), range(i + 1, 8)):
            for j in range_:
                if r[j] == '.':
                    break
                if r[j] == cur:
                    if abs(i - j) > 1:
                        r[min(i, j):max(i, j)] = cur * abs(i - j)
                    break
    return ''.join(r)
