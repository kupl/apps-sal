def minimum(arr):
    smallest = None
    for i in arr:
        if smallest is None:
            smallest = i
        elif i < smallest:
            smallest = i
    return smallest


def maximum(arr):
    largest = 0
    for i in arr:
        if i > largest:
            largest = i
        else:
            largest = largest
    return largest
