def is_centered(arr, n):
    x = sum(arr)
    if x == n: return True
    for i in range(len(arr)>>1):
        x -= arr[i] + arr[-i-1]
        if x == n: return True
    return False
