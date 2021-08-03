
def minimum(arr):
    min = None
    for i in arr:
        if min == None:
            min = i
        elif i < min:
            min = i
    return min


def maximum(arr):
    max = None
    for i in arr:
        if max == None:
            max = i
        elif i > max:
            max = i
    return max
