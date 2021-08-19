def sum_array(arr):
    return (lambda x: sum(x) - min(x) - max(x) * bool(x[1:]))(arr or [0])
