def is_sorted_and_how(arr):
    if arr[-1] > arr[0]:
        last = arr[0]
        for n in arr[1:]:
            if n < last:
                return "no"
            last = n
                
        return "yes, ascending"
        
    else:
        last = arr[0]
        for n in arr[1:]:
            if n > last:
                return "no"
            last = n
                
        return "yes, descending"

