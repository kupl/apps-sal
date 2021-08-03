def remove_smallest(numbers):
    arr = numbers.copy()
    if len(arr) == 0:
        return(arr)
    x = arr.index(min(arr))
    arr.pop(x)
    return(arr)
