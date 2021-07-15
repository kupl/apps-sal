def cube_times(times):
    times = sorted(times)
    return (round(sum(times[1:-1])/3,2), times[0])
