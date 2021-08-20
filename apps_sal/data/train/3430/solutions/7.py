def lowest_temp(s):
    return min(map(int, s.split()), default=None)
