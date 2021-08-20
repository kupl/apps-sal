def past(h, m, s):
    return 1000 * sum((unit * 60 ** power for (power, unit) in enumerate([s, m, h])))
