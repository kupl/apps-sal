def is_sorted_and_how(arr):
    arr_up = arr[0]
    arr_down = arr[0]
    check = 1
    for x in range(len(arr)):
        if arr[x] > arr_up:
            arr_up = arr[x]
            check += 1
    if check == len(arr):
        return 'yes, ascending'
    check = 1
    for x in range(len(arr)):
        if arr[x] < arr_down:
            arr_down = arr[x]
            check += 1
    if check == len(arr):
        return 'yes, descending'
    else:
        return 'no'
        
        


