def parse(data):
    action = {'i': lambda v, r: v + 1, 'd': lambda v, r: v - 1, 's': lambda v, r: v * v, 'o': lambda v, r: r.append(v) or v}
    (v, r) = (0, [])
    for a in data:
        v = action[a](v, r) if a in action else v
    return r
