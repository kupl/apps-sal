def cog_RPM(l, i):
    return [(-1 + (i + 1) % 2 * 2) * l[i] / l[0], (-1 + (len(l) - i) % 2 * 2) * l[i] / l[-1]]
