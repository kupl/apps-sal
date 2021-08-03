from re import findall


def moment_of_time_in_space(moment):
    time = sum(map(int, findall("\d", moment)))
    space = len(findall("[^1-9]", moment))
    states = [False for _ in range(3)]
    if time > space:
        states[2] = True
    elif time < space:
        states[0] = True
    else:
        states[1] = True
    return states
