def is_sorted_and_how(arr):
    b = 0
    
    for x in range(0, len(arr) -1):
        if arr[x] < arr[x+1]:
            b += 1
            if b == len(arr) -1:
                return "yes, ascending"
    b = 0
    for x in range(0, len(arr) -1):
        if arr[x] > arr[x+1]:
            b += 1
            if b == len(arr) -1:
                return "yes, descending"
                
        else: 
            return "no"
        
        

