def f(n, m):
    times = n // m
    extra = n % m
    sum_mini_series = (m - 1) * (m - 1 + 1) // 2
    sum_extra = extra * (extra + 1) // 2
    return sum_mini_series * times + sum_extra
