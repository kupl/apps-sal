def trouble(arr, t):
    for i in range(len(arr) - 1):
        if arr[i] + arr[i + 1] == t:
            return trouble(arr[:i + 1] + arr[i + 2:], t)
    return arr
