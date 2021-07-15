def multiple_of_index(arr):
    return [case for i, case in enumerate(arr) if i > 0 and case % i == 0]
