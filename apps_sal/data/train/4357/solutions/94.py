def nth_smallest(arr, pos):
    smallest = [0]
    small = 0
    for i in range(len(arr)):
        smallest.append(min(arr))
        arr.pop(arr.index(min(arr)))
    return smallest[pos]
