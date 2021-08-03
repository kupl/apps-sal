def lowest_temp(t):
    if t == '':
        return None
    t = t.split()
    low = int(t[0])
    for i in t:
        if int(i) < low:
            low = int(i)
    return low
