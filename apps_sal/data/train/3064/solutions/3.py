def transpose(arr):
    lst = []
    if len(arr) == 0:
        return arr
    for i in range(len(arr[0])):
        lst.append([arr[j][i] for j in range(len(arr))])
    return [[]] if not lst else lst
