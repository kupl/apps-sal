def series_sum(n):
    # term = 3n+1
    if n == 0:
        term = 0
    elif n > 0:
        term = 1
        for i in range(1, n):
            term += 1 / (3 * i + 1)
        sumterm = float("{:.2f}".format(term))
    return "%0.2f" % term
