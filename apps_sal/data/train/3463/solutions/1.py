def sum_times_tables(table, a, b):
    s = 0
    for i in range(a, b + 1):
        s = s + i * sum(table)
    return s
