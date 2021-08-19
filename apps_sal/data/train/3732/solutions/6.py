def is_madhav_array(arr):
    print(arr)
    if len(arr) < 3:
        return False
    i = 1
    k = 2
    while i < len(arr):
        t = 0
        for j in range(k):
            if i > len(arr) - 1:
                return False
            t += arr[i]
            i += 1
        if arr[0] != t:
            return False
        else:
            k += 1
    return True
