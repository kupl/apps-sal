def box(coords):
    (L1, L2) = zip(*coords)
    return {'nw': [max(L1), min(L2)], 'se': [min(L1), max(L2)]}
