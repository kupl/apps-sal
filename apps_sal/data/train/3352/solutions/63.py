def find_longest(arr):
    l = 0
    a = 0
    ind = 0
    for i in range(len(arr)):
        a = str(arr[i])
        if l < len(a):
            l = len(a)
            ind = i
    return arr[ind]
