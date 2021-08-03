def pattern(n, y=1, *args):
    if n < 1:
        return ""
    if y < 1:
        y = 1

    p = [" " * i + str((i + 1) % 10) + " " * (2 * n - 3 - 2 * i) + str((i + 1) % 10) + " " * i for i in range(n - 1)] + \
        [" " * (n - 1) + str(n % 10) + " " * (n - 1)] + \
        [" " * i + str((i + 1) % 10) + " " * (2 * n - 3 - 2 * i) + str((i + 1) % 10) + " " * i for i in range(n - 2, -1, -1)]

    return "\n".join(p + p[1:] * (y - 1))
