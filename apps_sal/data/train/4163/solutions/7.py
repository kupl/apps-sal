def is_centered(arr, n):
    return any(
        sum(arr[i:len(arr) - i]) == n for i in range(len(arr) // 2 + 1)
    )
