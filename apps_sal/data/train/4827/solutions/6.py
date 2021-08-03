from math import sqrt


def stats_disc_distr(distrib):
    if round(sum(count[1] for count in distrib), 3) != 1:
        if not all(isinstance(count[0], int) for count in distrib):
            return "It's not a valid distribution and furthermore, one or more variable value are not integers"
        else:
            return "It's not a valid distribution"

    if not all(isinstance(count[0], int) for count in distrib):
        return "All the variable values should be integers"

    expected = sum(event * prob for event, prob in distrib)
    variance = sum((event - expected)**2 * prob for event, prob in distrib)
    standard = sqrt(variance)

    return [expected, variance, standard]
