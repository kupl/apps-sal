def sum_array(arr):
    if arr == [] or arr == None:
        return 0
    elif len(arr) < 3:
        return 0
    arr = sorted(arr)
    result = 0
    arr.pop()
    arr.pop(0)
    print(arr)
    for i in arr:
        result += i
    return result
