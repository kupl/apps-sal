def is_sorted_and_how(arr):
    decend_Counter = 0;
    accend_Counter = 0;
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            decend_Counter += 1
        if arr[i] < arr[i + 1]:
            accend_Counter += 1
    if (decend_Counter == len(arr) - 1):
        return "yes, descending"
    elif (accend_Counter == len(arr) - 1):
        return "yes, ascending"
    else:
        return "no"
                
    return 1
