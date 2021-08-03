def tetris(arr):
    d, c = {}, 0
    for i, j in enumerate(arr):
        t, dt = j[1:].replace('R0', 'L0'), d.values()
        d[t] = d.get(t, 0) + int(j[0])
        if len(dt) == 9 and all(dt):
            m = min(d.values())
            d = {k: l - m for k, l in d.items()}
            c += m
        if d[t] >= 30:
            break
    return c
