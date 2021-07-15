def can_jump(arr):
    if len(arr) <= 1 or arr[0] == 0:
        return False
    if arr[0] >= len(arr):
        return True
    return any(can_jump(arr[i+1:]) for i in range(arr[0]))

