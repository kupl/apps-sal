def find_average(arr):
    s = 0
    l = len(arr)
    for i in arr:
        s = s + i
    return s // l
