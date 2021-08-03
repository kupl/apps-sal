def is_centered(arr, n):
    for i in range(len(arr) // 2 + 1):
        if sum(arr[i:len(arr) - i]) == n:
            return True
    return False
