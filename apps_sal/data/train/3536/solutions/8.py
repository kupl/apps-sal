def cog_RPM(cogs, i):
    x, y = cogs[i] / cogs[0], cogs[i] / cogs[-1]
    if i & 1: x = -x
    if len(cogs) - 1 - i & 1: y = -y
    return [x, y]
