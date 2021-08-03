def sum_array(arr):
    if not arr:
        return 0
    arr2 = []
    arr.sort()
    index = -1
    for i in arr:
        index += 1
        if(index > 0 and index < len(arr) - 1):
            arr2.append(i)
    return sum(arr2)
