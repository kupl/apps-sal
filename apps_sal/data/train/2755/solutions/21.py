def multiple_of_index(arr):
    return [x[1] for x in enumerate(arr) if x[0] and (not x[1] % x[0])]
