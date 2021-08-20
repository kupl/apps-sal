def multiple_of_index(arr):
    return [x for (index, x) in enumerate(arr) if index != 0 and x % index == 0]
