def lowest_temp(t):
    return min((int(x) for x in t.split())) if t else None
