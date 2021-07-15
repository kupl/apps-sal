def race(v1, v2, g):
    if v2 <= v1:
        return None
    total = g / (v2 - v1)
    return [int(total), int(total * 60) % 60, int(total * 3600) % 60]
