def stats_disc_distr(distrib):
    print(sum(p for x, p in distrib))
    if abs(sum(p for x, p in distrib) - 1) > 1e-4:
        if not all(x % 1 == 0 for x, p in distrib):
            return "It's not a valid distribution and furthermore, one or more variable value are not integers"
        return "It's not a valid distribution"
    if not all(x % 1 == 0 for x, p in distrib):
        return "All the variable values should be integers"

    mean = sum(x * p for x, p in distrib)
    var = sum((x - mean) ** 2 * p for x, p in distrib)
    std_dev = var ** 0.5
    return [mean, var, std_dev]
