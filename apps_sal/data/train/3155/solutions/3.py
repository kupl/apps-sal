def fit_in(a, b, m, n):
    # check first dimension
    if max(a, b) > min(m, n):
        return False

    # check second dimension
    if sum([a, b]) > max(m, n):
        return False

    return True
