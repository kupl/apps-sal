def bubblesort_once(lst):
    arr = lst[:]
    for i in range(len(arr)-1):
        arr[i], arr[i+1] = sorted([arr[i], arr[i+1]])
    return arr
