def multiple_of_index(arr):
    return [e for (i, e) in enumerate(arr) if i and (not e % i)]
