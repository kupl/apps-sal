def minimum(arr):
    arr.sort()
    return arr[0]

def maximum(arr):
    arr.sort()
    arr.reverse()
    return arr[0]
