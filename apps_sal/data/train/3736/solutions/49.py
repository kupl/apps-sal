def minimum(arr):
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    return min
            
def maximum(arr):
    max = 0
    for i in arr:
        if i > max:
            max = i
    return max
