def sum_times_tables(table, a, b):
    total = 0
    for x in range(a, b + 1):
        total += sum(list([x * n for n in table]))
    return total
