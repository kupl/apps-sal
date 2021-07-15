def lowest_temp(t):
    if t:
        return min([int(x) for x in t.split()])
    else:
        return None

