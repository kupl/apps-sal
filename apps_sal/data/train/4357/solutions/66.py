def nth_smallest(arr, pos):
    m=0
    while pos!=0:
        m=min(arr)
        arr.pop(arr.index(m))
        pos-=1
    return m
