def sum_of_intervals(a): return len(set.union(*(set(range(*i))for i in a)))
