def seven(m):
    steps = 0
    while m >= 100:
        m = int(str(m)[:-1]) - 2 * int(str(m)[-1])
        steps = steps + 1
    return m, steps
