def stats_disc_distr(distrib):
    values, probs = zip(*distrib)
    probs_is_not_one = (abs(sum(probs) - 1) > 1e-8)
    values_are_not_ints = any(value % 1 for value in values)
    if probs_is_not_one and values_are_not_ints:
        return "It's not a valid distribution and furthermore, one or more variable value are not integers"
    elif values_are_not_ints:
        return "All the variable values should be integers"
    elif probs_is_not_one:
        return "It's not a valid distribution"
    mean = sum((value * prob) for value, prob in distrib)
    var = sum(((value - mean)**2 * prob) for value, prob in distrib)
    std_dev = var**0.5
    return [mean, var, std_dev]
