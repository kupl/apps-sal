def cog_RPM(cogs, n):
    output = []
    if n % 2 == 0:
        a = 1
        if (len(cogs) % 2 - 1) == 0:
            b = 1
        else:
            b = -1
    else:
        a = -1
        if (len(cogs) - 1) % 2 == 0:
            b = -1
        else:
            b = 1
    output.append(cogs[n] / cogs[0] * a)
    output.append(cogs[n] / cogs[-1] * b)
    return output
