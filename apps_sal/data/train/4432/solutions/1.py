def can_jump(arr):
    last = len(arr)
    for i in reversed(range(len(arr) - 1)):
        if arr[i] >= last - i:
            last = i
    return not last
