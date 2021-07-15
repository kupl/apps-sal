sum_array = lambda arr: (lambda x: sum(x) - min(x) - max(x) * bool(x[1:]))(arr or [0])
