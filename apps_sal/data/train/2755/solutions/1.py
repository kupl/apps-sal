def multiple_of_index(arr):
    return [val for index, val in enumerate(arr) if index and val % index == 0]
