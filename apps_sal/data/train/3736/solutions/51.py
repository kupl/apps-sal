def minimum(arr):
    min = float('inf')
    for num in arr:
        if num < min:
            min = num
    return min

def maximum(arr):
    max = float('-inf')
    for num in arr:
        if num > max:
            max = num
    return max
