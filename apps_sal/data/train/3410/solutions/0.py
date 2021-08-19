def scratch(lottery):
    return sum((int(n) for lot in lottery for (a, b, c, n) in [lot.split()] if a == b == c))
