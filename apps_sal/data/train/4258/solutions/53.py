def series_sum(n):
    summa = sum([1/(1+3*x) for x in range(n)])
    return f"{summa:.{2}f}"
