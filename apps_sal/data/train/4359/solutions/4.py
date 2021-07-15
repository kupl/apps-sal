def cube_times(times):
    record_time = min(times)
    slowest_time = max(times)
    average = 0
    for time in times:
        if time == record_time or time == slowest_time:
            pass
        else:
            average += time
    rounded_time = round(average / 3, 2)
    return (rounded_time, record_time)
