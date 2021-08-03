def capitalize(s, ind):
    arr = list(s)
    for i in range(len(s)):
        if i in ind:
            arr[i] = arr[i].upper()
    return ''.join(arr)
