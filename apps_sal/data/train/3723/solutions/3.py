def array_change(arr):
    count = 0
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            count += arr[i] - arr[i + 1] + 1
            arr[i + 1] += arr[i] - arr[i + 1] + 1
    return count
