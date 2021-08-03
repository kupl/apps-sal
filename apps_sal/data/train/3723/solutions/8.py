def array_change(arr):
    move = 0
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            move += arr[i - 1] - arr[i] + 1
            arr[i] += arr[i - 1] - arr[i] + 1
    return move
