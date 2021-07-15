def capitalize(s,ind):
    arr = list(s)
    for i in ind:
        if i <= len(arr):
            arr[i] = arr[i].upper()
    return ''.join(arr)
