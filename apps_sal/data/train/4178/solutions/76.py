def min_sum(arr):
    count = 0
    while len(arr)>0:
        count += max(arr)*min(arr)
        arr.remove(max(arr))
        arr.remove(min(arr))
    return count
