def lowest_temp(t):
    return min([int(tm) for tm in t.split()]) if t else None
