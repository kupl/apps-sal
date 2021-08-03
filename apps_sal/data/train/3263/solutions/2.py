def solve(arr):
    sorted_arr = sorted(arr, reverse=True)
    sorted_as_min = list(map(time_to_minutes, sorted_arr))
    windows = list(zip(sorted_as_min, sorted_as_min[1:]))
    differences = list(map(lambda w: w[0] - w[1], windows))
    differences.append(24 * 60 - sorted_as_min[0] + sorted_as_min[-1])
    return minutes_to_time(max(differences) - 1)


def time_to_minutes(time):
    (hr, min) = time.split(":")
    return int(hr) * 60 + int(min)


def minutes_to_time(minutes):
    return "{H:0=2d}:{M:0=2d}".format(H=minutes // 60, M=minutes % 60)
