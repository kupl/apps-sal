def f(n, m):
    n, m = int(n), int(m)

    whole_runs = n / m
    leftovers = n % m

    per_run = (m - 1) * (m - 1 + 1) / 2
    leftovers_sum = leftovers * (leftovers + 1) / 2

    return whole_runs * per_run + leftovers_sum
