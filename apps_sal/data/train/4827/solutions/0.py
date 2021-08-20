def stats_disc_distr(distrib):
    err = check_errors(distrib)
    if not err:
        mean = sum((x[0] * x[1] for x in distrib))
        var = sum(((x[0] - mean) ** 2 * x[1] for x in distrib))
        std_dev = var ** 0.5
    return [mean, var, std_dev] if not err else err


def check_errors(distrib):
    errors = 0
    if not isclose(sum((x[1] for x in distrib)), 1):
        errors += 1
    if not all((isinstance(x[0], int) for x in distrib)):
        errors += 2
    if errors > 0:
        return {1: "It's not a valid distribution", 2: 'All the variable values should be integers', 3: "It's not a valid distribution and furthermore, one or more variable value are not integers"}[errors]


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
