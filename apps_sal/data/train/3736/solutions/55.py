def minimum(arr):
    # your code here...
    val = arr[0]
    for i in arr:
        if i < val:
            val = i
    return val


def maximum(arr):
    #...and here
    val = arr[0]
    for i in arr:
        if i > val:
            val = i
    return val
