def stats_disc_distr(distrib):
    is_valid_distribution = lambda d: abs(sum(px for x, px in d) - 1) < 1e-8
    are_events_integers = lambda d: all(isinstance(x, (int, float)) and float(x).is_integer() for x, px in d)
    events, probabilities = are_events_integers(distrib), is_valid_distribution(distrib)
    if not events and not probabilities:
        return "It's not a valid distribution and furthermore, one or more variable value are not integers"
    elif not probabilities:
        return "It's not a valid distribution"
    elif not events:
        return "All the variable values should be integers"
    mean = sum(x * px for x, px in distrib)
    var = sum((x - mean) ** 2 * px for x, px in distrib)
    std_dev = var ** .5
    return [mean, var, std_dev]
