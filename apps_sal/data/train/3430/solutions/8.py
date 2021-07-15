def lowest_temp(t):
    if not t:
        return None
    return min(int(x) for x in t.split())
