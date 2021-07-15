def minimum(arr):
    mini = arr[0]
    for num in arr:
        if num < mini: mini = num
    return mini

def maximum(arr):
    maxi = arr[0]
    for num in arr:
        if num > maxi: maxi = num
    return maxi
