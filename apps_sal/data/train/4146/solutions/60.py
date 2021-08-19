def is_sorted_and_how(arr):
    print(arr)
    d = True
    a = True
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            d = False
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            a = False
    if d:
        return 'yes, descending'
    elif a:
        return 'yes, ascending'
    else:
        return 'no'
