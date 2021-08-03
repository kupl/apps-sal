def cog_RPM(cogs, n):
    return [cogs[n] / cogs[0] * (-1)**n, cogs[n] / cogs[-1] * (-1)**(len(cogs) - n - 1)]
