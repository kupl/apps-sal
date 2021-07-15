def T(n):
    return n * (n + 1) // 2

def sum_times_tables(table,a,b):
    return sum(table) * (T(b) - T(a - 1))
