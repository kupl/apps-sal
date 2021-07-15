def moment_of_time_in_space(moment):
    time = 0
    space = 0
    for ch in moment:
        if ch == '0' or not ch.isdigit():
            space += 1
        elif ch in '123456789':
            time += int(ch)
    return [time < space, time == space, time > space]
