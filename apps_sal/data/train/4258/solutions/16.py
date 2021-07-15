def series_sum(n):
    return f"{sum(1/x for x in range(1,(n*3)-1,3)):.2f}"
