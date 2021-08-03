def multiple_of_index(arr):
    result = []

    for i in range(1, len(arr)):
        if not arr[i] % i:
            result.append(arr[i])

    return result
