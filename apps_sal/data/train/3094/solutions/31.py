(sum_good, sum_array) = (lambda x: sum(x) - min(x) - max(x) * bool(x[1:]), lambda arr: sum_good(arr or [0]))
