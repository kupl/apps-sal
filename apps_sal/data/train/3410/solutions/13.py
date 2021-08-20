def scratch(lottery):
    return sum((int(n) for combi in lottery for (a, b, c, n) in [combi.split()] if a == b == c))
