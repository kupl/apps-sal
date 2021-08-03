def is_sorted_and_how(arr):
    if arr[0] > arr[1]:
        for i in range(len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                return('no')
        return('yes, descending')
    else:
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                return('no')
        return('yes, ascending')
