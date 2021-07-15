def multiple_of_index(arr):
    return [v for i,v in enumerate(arr) if i > 0 and v % i == 0]
