def solve(xs, n):
    rs = set()
    for x in xs:
        for r in list(rs):
            rs.add((r + x) % n)
        rs.add(x % n)
    return 0 in rs
