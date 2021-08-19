def multiple_of_index(arr):
    return [v for (k, v) in enumerate(arr) if k > 0 and (not v % k)]
