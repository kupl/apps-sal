def solve(arr):
    array = []
    for item in arr:
        if item in array:
            array.remove(item)
            array.append(item)
        else:
            array.append(item)
    return array
