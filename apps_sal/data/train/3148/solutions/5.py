def simplify(p):
    x = 0
    y = 0
    r = [(0, 0)]
    for i in p:
        if i == '<':
            x -= 1
        if i == '>':
            x += 1
        if i == '^':
            y += 1
        if i == 'v':
            y -= 1
        if (x, y) in r:
            p = p[:r.index((x, y))] + p[len(r):]
            r = r[:r.index((x, y))]
        r.append((x, y))

    return p
