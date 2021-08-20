def is_madhav_array(arr):
    if len(arr) < 2:
        return False
    x = 1 + 8 * len(arr)
    if int(x ** 0.5) ** 2 != x:
        return False
    y = (int(x ** 0.5) - 1) // 2
    s = arr[0]
    for i in range(2, y + 1):
        j = i * (i - 1) // 2
        if sum(arr[j:j + i]) != s:
            return False
    return True
