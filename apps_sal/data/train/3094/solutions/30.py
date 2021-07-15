sum_good = lambda x: sum(x) - min(x) - max(x) * bool(x[1:])
sum_array = lambda arr: sum_good(arr or [0])

