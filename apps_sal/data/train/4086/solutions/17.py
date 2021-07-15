def first_non_consecutive(arr):
    for index in range(len(arr)-1):
        if abs(arr[index+1] - arr[index]) != 1:
            return arr[index+1]
    return None
