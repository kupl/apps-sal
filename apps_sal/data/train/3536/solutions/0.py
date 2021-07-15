def cog_RPM(cogs, n):
    return [
        cogs[n] / cogs[0] * (-1 if n % 2 else 1),
        cogs[n] / cogs[-1] * (1 if (len(cogs) - n) % 2 else -1),
    ]
