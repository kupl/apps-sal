def multiple_of_index(arr):
    return [a for i, a in enumerate(arr) if i > 0 and a % i == 0]
