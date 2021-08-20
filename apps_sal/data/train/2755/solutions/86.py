def multiple_of_index(arr):
    return [arr for (ind, arr) in enumerate(arr) if ind > 0 and arr % ind == 0]
