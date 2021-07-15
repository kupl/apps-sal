def box(coords):
    return {
        'nw': [max(x for x, _ in coords), min(y for _, y in coords)],
        'se': [min(x for x, _ in coords), max(y for _, y in coords)],
    }
