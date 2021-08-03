def box(coords):
    a = min(i[0] for i in coords)
    b = max(i[0] for i in coords)
    c = min(i[1] for i in coords)
    d = max(i[1] for i in coords)
    return {'nw': [b, c], 'se': [a, d]}
