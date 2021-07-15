def nth_smallest(arr, pos):
    while pos>1:
        arr.remove(min(arr))
        if len(arr)<2:
            return arr[0]
        pos-=1
    return min(arr)
