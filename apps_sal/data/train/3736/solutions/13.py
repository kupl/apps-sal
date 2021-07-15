def minimum(arr):
    m = arr[0]
    for i in arr:
        if m > i:
            m = i
    return m
        

def maximum(arr):
    t = arr[0]
    for i in arr:
        if i > t:
            t = i
    return t
