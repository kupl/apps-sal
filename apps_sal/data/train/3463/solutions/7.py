def sum_times_tables(table, a, b):
    return sum((x * y for x in table for y in range(a, b + 1)))
