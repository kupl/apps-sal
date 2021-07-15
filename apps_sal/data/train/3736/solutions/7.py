def maximum(arr):
    maximum = arr[0]
    for i in arr:
        if i > maximum:
            maximum = i
    return maximum 
        

def minimum(arr):
    minimum = arr[0]
    for i in arr:
        if i < minimum:
            minimum = i
    return minimum 
