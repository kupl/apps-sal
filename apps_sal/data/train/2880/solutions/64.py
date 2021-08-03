def seven(m):
    n_steps = 0

    while m > 99:
        x, y = m // 10, m % 10
        m = x - (2 * y)

        n_steps += 1

    return m, n_steps
