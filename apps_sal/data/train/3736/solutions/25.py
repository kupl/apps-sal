def minimum(arr):
    # your code here...
    smallest = None
    for i in arr:
        if smallest is None:
            smallest = i
        elif i < smallest:
            smallest = i
    return smallest


def maximum(arr):
    #...and here
    largest = 0
    for i in arr:
        if i > largest:
            largest = i
        else:
            largest = largest
    return largest
