def array_change(arr):
    moves = 0
    for i in range(len(arr) - 1):
        if arr[i + 1] <= arr[i]:
            diff = arr[i] - arr[i + 1] + 1
            arr[i + 1] += diff
            moves += diff
    return moves
