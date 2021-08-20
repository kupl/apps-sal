def seven(m):
    steps = 0
    r = m
    numstr = str(r)
    while r > 99:
        steps += 1
        r = int(numstr[0:-1]) - 2 * int(numstr[-1])
        numstr = str(r)
    return (r, steps)
