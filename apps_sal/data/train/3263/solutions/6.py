def solve(times):

    def to_minutes(time):
        (hh, mm) = time.split(':')
        return int(hh) * 60 + int(mm)
    times = sorted((to_minutes(time) for time in times))
    times.append(times[0] + 24 * 60)
    result = max((b - a - 1 for (a, b) in zip(times, times[1:])))
    return '{:02d}:{:02d}'.format(*divmod(result, 60))
