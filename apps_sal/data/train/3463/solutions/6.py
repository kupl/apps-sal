def sum_times_tables(table, a, b):
    return sum(table) * (summa(b) - summa(a - 1))


def summa(n):
    return n * (n + 1) / 2
