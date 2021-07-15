def count_squares(lines):
    
    sides = {(r, c):v for r, row in enumerate(lines) for c, v in enumerate(row) if v in '+-|'}
    nodes = sorted(k for k, v in sides.items() if v == '+')[::-1]

    sideh = lambda r, c, target: all(sides.get((r, c + cc), ' ') in '+-' for cc in range(target - c))
    sidev = lambda r, c, target: all(sides.get((r + rr, c), ' ') in '+|' for rr in range(target - r))

    t = 0
    while nodes:
        r, c = nodes.pop()
        for cc in [p[1] for p in nodes if r == p[0] and sideh(r, c, p[1])]:
            rr = r + cc - c
            if (rr, c) in nodes and (rr, cc) in nodes and sidev(r, c, rr) and sidev(r, cc, rr) and sideh(rr, c, cc):
                t += 1
    return t
