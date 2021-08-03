def conjugate(v):
    h = i = v[:-1]
    if h[-1] == 'i':
        h = h[:-1] + 'e'
        i = v[:-2]
    return {v: [v[:-2] + 'o', h + 's', h, v[:-1] + 'mos', i + 'is', h + 'n']}
