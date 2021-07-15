def box(coords):
    lat, long = zip(*coords)
    return {"nw": [max(lat), min(long)], "se": [min(lat), max(long)]}
