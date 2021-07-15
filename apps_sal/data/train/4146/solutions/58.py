def is_sorted_and_how(arr):
    order = 0
    i = 0
    
    for num in arr:
        hold = arr[i]
        
        if i + 1 < len(arr):
            if hold <= arr[i + 1]:
                order += 1
            if hold >= arr[i + 1]:
                order -= 1
            
        i += 1
              
    if order == len(arr) - 1: return 'yes, ascending'
    if order * -1 == len(arr) - 1: return 'yes, descending'
    else: return 'no'
