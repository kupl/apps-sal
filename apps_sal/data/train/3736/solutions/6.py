def minimum(arr):
    current_best = arr[0]
    for i in arr:
        if i < current_best:
            current_best = i
    return current_best

def maximum(arr):
    current_best = arr[0]
    for i in arr:
        if i > current_best:
            current_best = i
    return current_best
