from statistics import mean


def cube_times(times):
    return (round(mean(sorted(times)[1:4]), 2), min(times))
