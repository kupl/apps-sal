def multiple_of_index(arr):
    return [i for (idx, i) in enumerate(arr) if idx and (not i % idx)]
