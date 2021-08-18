def rat_at(n):
    if n == 0:
        return 1, 1
    line = 1
    tot = 0
    while tot <= n:
        tot += 2**line
        line += 1
    if line > 1:
        line -= 1
    route = ''
    b = 2**line
    pos = n + 1 - 2**line
    while b > 1:
        if pos < b // 2:
            route += 'l'
            b = b // 2
        else:
            route += 'r'
            b = b // 2
            pos -= b
    a, b = 1, 1
    for c in route:
        if c == 'l':
            a, b = a, a + b
        else:
            a, b = a + b, b
    return a, b


def index_of(a, b):
    aa = a
    bb = b
    route = ''
    while not (aa == 1 and bb == 1):
        if aa > bb:
            aa = aa - bb
            route = 'r' + route
        else:
            bb = bb - aa
            route = 'l' + route
    above = 0
    for i in range(len(route)):
        above += 2**i
    pos = [0, 2**len(route) - 1]
    for c in route:
        if c == 'l':
            pos[1] = pos[1] - (pos[1] + 1 - pos[0]) // 2
        else:
            pos[0] = pos[0] + (pos[1] + 1 - pos[0]) // 2
    print(("a: {0}, b: {1}, above: {2}, pos: {3}, route: {4}".format(a, b, above, pos, route)))
    return above + pos[0]
