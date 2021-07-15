def minimum(arr):
    base = arr[0]
    if len(arr) == 1:
            return base
    else:
        for number in arr:
            if number < base:
                base = number
        return base

def maximum(arr):
    base = arr[0]
    if len(arr) == 1:
            return base
    else:
        for number in arr:
            if number > base:
                base = number
        return base
