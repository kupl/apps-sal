def peaceful_yard(yard, min_distance):
    cats = [x+y*1j for y, l in enumerate(yard) for x, c in enumerate(l) if c != '-']
    return all(abs(a - b) >= min_distance for i, a in enumerate(cats) for b in cats[:i])
