def first_non_consecutive(arr):
    i = 0
    for num in range(arr[0], arr[len(arr) - 1]):
        if num != arr[i]:
            return arr[i]
        i += 1
    return None
