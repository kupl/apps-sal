def possible_positions(pos):
    (rows, cols) = ('abcdefgh', '12345678')
    row = rows.index(pos[0])
    col = cols.index(pos[1])
    M = [(a, b) for a in [1, -1] for b in [2, -2]]
    P = [(row + rr, col + cc) for (rr, cc) in M + [e[::-1] for e in M]]
    return sorted((rows[r] + cols[c] for (r, c) in P if 0 <= r <= 7 and 0 <= c <= 7))
