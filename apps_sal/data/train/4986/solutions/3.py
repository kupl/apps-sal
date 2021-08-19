def f(n, m):
    # Either n or m seems to have a floating-point representation in one of the official tests.
    # Since it's a .0, converting to int is fine.
    n, m = int(n), int(m)

    # n=14, m=5  ->  2 whole runs, plus the 4 first modulos
    whole_runs = n / m
    leftovers = n % m

    # n=5, m=5  ->  1+2+3+4+0 == (m-1)/(m-1+1)/2
    per_run = (m - 1) * (m - 1 + 1) / 2
    leftovers_sum = leftovers * (leftovers + 1) / 2

    return whole_runs * per_run + leftovers_sum
