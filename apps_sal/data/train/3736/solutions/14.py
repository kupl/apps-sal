def minimum(arr):
    min = arr[0]
    while len(arr) > 1:
        if arr[1] < min:
            min = arr[1]
            arr.pop(0)
        else:
            arr.pop(1)
    return min

def maximum(arr):
    max = arr[0]
    while len(arr) > 1:
        if arr[1] > max:
            max = arr[1]
            arr.pop(0)
        else:
            arr.pop(1)
    return max

