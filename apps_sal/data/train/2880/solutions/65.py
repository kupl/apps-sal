def seven(m):
    n_steps = 0

    while len(str(m)) > 2:
        m_str = str(m)
        x, y = int(str(m)[:-1]), int(str(m)[-1])
        m = x - (2 * y)

        n_steps += 1

    return m, n_steps
