def lowest_temp(s):
    return min((int(x) for x in s.split()), default=None)
