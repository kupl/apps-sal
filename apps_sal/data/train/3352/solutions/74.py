def find_longest(arr):
    ln = 0
    index = 0
    for i in arr:
        listln = len(str(i))
        if listln > ln:
            ln = listln
            index = arr.index(i)
    return arr[index]
