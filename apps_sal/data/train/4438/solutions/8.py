def middle_point(*coords):
    c = sorted((coords[i::3] for i in range(3)), key=lambda c: -len(set(c)))[0]
    return c.index(sorted(c)[1]) + 1
