def is_sorted_and_how(arr):
    # your code here
    if(sorted(arr) == arr):
        result = 'yes, ascending'
    elif (sorted(arr, reverse = True) == arr):
        result = 'yes, descending'
    else:
        result = 'no'
        
    return result
