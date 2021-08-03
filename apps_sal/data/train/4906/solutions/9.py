def traffic_lights(road, n):
    a, b, c = 'GGGGGORRRRR', 'ORRRRRGGGGG', 'RRRRRGGGGGO'
    r, p = [road], 0
    for i in range(1, n + 1):
        t = [a[i % 11] if x == 'G' else b[i % 11] if x == 'O' else c[i % 11] if x == 'R' else x for x in road]
        if p < len(road) - 1:
            if t[p + 1] not in 'RO':
                p += 1
                t[p] = 'C'
            elif t[p + 1] in 'RO':
                t[p] = 'C'
        t[0] = 'C' if p == 0 else '.'
        r.append(''.join(t))
    return r
