def is_sorted_and_how(arr):
    # your code here
    isAllNeg = True
    isAllPos = True
    
    for i in range(len(arr) - 1):
        isAllPos = isAllPos and arr[i + 1] - arr[i] > 0
        isAllNeg = isAllNeg and arr[i + 1] - arr[i] < 0
        
    if isAllPos:
        return "yes, ascending"
    elif isAllNeg:
        return "yes, descending"
    else:
        return 'no'
