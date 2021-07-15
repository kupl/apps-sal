def stats_disc_distr(distrib):
    dist = abs(sum(px for x, px in distrib) - 1) < 0.00001
    all_int = all(isinstance(x, int) for x, px in distrib)
    if not dist:
        if not all_int:
            return "It's not a valid distribution and furthermore, one or more variable value are not integers"
        return "It's not a valid distribution"
    if not all_int:
        return "All the variable values should be integers"
    u = sum(x * px for x, px in distrib)
    o2 = sum(abs((x - u) ** 2 * px) for x, px in distrib)
    o = o2 ** 0.5
    return [u, o2, o]
