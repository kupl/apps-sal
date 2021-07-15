def cog_RPM(cogs, idx):
    first = cogs[idx] / cogs[0] * [1, -1][idx & 1]
    last = cogs[idx] / cogs[-1] * [1, -1][(len(cogs) - idx - 1) & 1]
    return [first, last]
