def sum_array(arr):
    if arr==[] or arr == None or len(arr) == 1:
        return 0
    else:
        mini = min(arr)
        maxi = max(arr)
        max_index = arr.index(maxi)
        min_index = arr.index(mini)
        arr[max_index] = 0
        arr[min_index] = 0
        ttl = 0
        for x in arr:
            ttl += x
    return ttl

