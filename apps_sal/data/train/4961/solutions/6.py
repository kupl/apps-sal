def box(coords):
    a = [n for n,m in coords]
    b = [m for n,m in coords]
    
    return {'nw': [max(a), min(b)], 'se': [min(a), max(b)]}
