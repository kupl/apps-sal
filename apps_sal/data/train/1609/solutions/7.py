sum_of_intervals=lambda a:len(set.union(*(set(range(*i))for i in a)))
