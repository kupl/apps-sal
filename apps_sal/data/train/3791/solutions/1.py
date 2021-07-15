def moment_of_time_in_space(moment):
    time = sum(int(c) for c in moment if c in "123456789")
    space = sum(c not in "123456789" for c in moment)
    return [time < space, time == space, time > space]
