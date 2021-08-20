def trouble(arr, t):
    i = 0
    while i < len(arr) - 1:
        if arr[i] + arr[i + 1] == t:
            del arr[i + 1]
        else:
            i += 1
    return arr
