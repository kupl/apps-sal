def cube_times(times):
    times.sort()
    mid = times[1:4]
    return ( round(sum(mid) / len(mid), 2), times[0])
