def is_sorted_and_how(arr):
    if arr[0] >= arr[1]:
        for i in range(1,len(arr)):
            if arr[i-1] < arr[i]:
                return "no"
        return "yes, descending"
    elif arr[0] <= arr[1]:
        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                return 'no'
        return "yes, ascending"
    else:
        return "no"
