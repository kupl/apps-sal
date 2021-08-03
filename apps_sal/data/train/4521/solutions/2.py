def numberOfSteps(steps, m):
    if m > steps:
        return -1
    c = 1
    while steps > 2 * m * c:
        c += 1
    return m * c
