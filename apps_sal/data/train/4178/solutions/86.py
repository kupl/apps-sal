def min_sum(arr):
    sumlist = []
    while len(arr) > 0:
        if len(arr) == 1:
            sumlist.append(arr)
        else:
            sumlist.append(max(arr) * min(arr))
            arr.remove(max(arr))
            arr.remove(min(arr))
    return sum(sumlist)
