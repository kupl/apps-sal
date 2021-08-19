def box(coords):
    (NS, EW) = zip(*coords)
    return {'nw': [max(NS), min(EW)], 'se': [min(NS), max(EW)]}
