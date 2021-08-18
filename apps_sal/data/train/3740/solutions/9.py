def sort_time(arr):
    arr = arr[:]
    result = []
    next = min(arr)
    while True:
        result.append(next)
        arr.remove(next)
        if not arr:
            break
        next = None
        for t in arr:
            if result[-1][1] <= t[0]:
                if next is None or next[0] > t[0]:
                    next = t
        if next is None:
            next = min(arr)

    return result
