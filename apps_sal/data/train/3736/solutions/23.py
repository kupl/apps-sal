def minimum(arr):
    minimum = arr[0]
    for i in range(0, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
    return minimum

def maximum(arr):
    maximum = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum
