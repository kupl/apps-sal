def solve(times):
    mins = sorted(int(t[:2])*60 + int(t[3:]) for t in set(times))
    mins += [mins[0] + 1440]
    max_time = max(b - a - 1 for a, b in zip(mins, mins[1:]))
    return '%02d:%02d' % divmod(max_time, 60)
