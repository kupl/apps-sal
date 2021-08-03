def numberOfSteps(steps, m):
    if m > steps:
        return -1
    abs_min_steps = int(steps / 2) + steps % 2
    steps_dif = abs_min_steps % m
    if (steps_dif):
        return (m - steps_dif) + abs_min_steps
    else:
        return abs_min_steps
