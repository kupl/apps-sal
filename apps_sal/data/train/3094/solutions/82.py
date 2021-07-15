def sum_array(arr):
    a = 0
    if arr == []:
        return 0
    if arr == None:
        return 0
    if len(arr)==1 or len(arr) == 2:
        return 0
    arr.sort()
    for i in range(len(arr)-2):
        a += arr[i+1]
    return a
