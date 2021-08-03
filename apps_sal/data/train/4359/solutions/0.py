def cube_times(times):
    return (round((sum(times) - (min(times) + max(times))) / 3, 2), min(times))
