def minimum(arr):
    a = 100000000000000000000000000000000000
    for i in range(len(arr)):
        if arr[i]<a:
            a = arr[i]
    return a
def maximum(arr):
    a = -1000000000000000000000000000000000000000000
    for i in range(len(arr)):
        if arr[i]>a:
            a = arr[i]
    return a
