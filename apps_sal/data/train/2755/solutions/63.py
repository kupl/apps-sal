def multiple_of_index(arr):
    matches = []
    index = 1
    for value in arr[1:]:
        if value % index == 0:
            matches.append(value)
        index += 1
    return matches
