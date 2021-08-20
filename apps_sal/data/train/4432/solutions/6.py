def can_jump(arr, i=0):
    return i >= len(arr) or (i < len(arr) - 1 and arr[i] and any((can_jump(arr, i + j) for j in range(1, arr[i] + 1))))
