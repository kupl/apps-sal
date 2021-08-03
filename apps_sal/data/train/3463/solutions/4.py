def sum_times_tables(table, a, b):
    n = sum(table)
    return n and sum(range(n * a, n * (b + 1), n))
