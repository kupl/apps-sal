def first_non_consecutive(arr):
    result = arr[0]
    for i in arr[1:]:
        if i - result != 1:
            return i
        result = i
