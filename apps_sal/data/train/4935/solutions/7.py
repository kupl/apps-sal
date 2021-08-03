def infected(s):
    infected = 0
    total = 0
    for land in s.split('X'):
        if '1' in land:
            infected += len(land)
        total += len(land)
    return infected / total * 100 if total > 0 else 0
