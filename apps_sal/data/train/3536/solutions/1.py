def cog_RPM(cogs, n):
    sign1 = -1 if n % 2 else 1
    sign2 = 1 if (len(cogs) - n) % 2 else -1
    return [sign1 * cogs[n] / cogs[0], sign2 * cogs[n] / cogs[-1]]
