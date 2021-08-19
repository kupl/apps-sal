def seven(m):
    steps = 0
    while len(str(m)) > 2:
        num = int(str(m)[-1])
        m = m // 10
        m = m - num * 2
        steps = steps + 1
    return (m, steps)
