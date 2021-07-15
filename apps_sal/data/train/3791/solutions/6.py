def moment_of_time_in_space(moment):
    time = int(moment[0]) + int(moment[1]) + int(moment[3]) + int(moment[4])
    space = 4 + moment.count("0")
    return [time < space, time == space, time > space]
