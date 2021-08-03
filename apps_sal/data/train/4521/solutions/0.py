def numberOfSteps(steps, m):
    if (steps < m):
        return -1

    if (steps % 2 == 0 and (steps / 2) % m == 0):
        return (steps / 2)

    return (steps / 2) + m - ((steps / 2) % m)
