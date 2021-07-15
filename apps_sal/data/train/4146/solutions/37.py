def is_sorted_and_how(arr):
    asc=False
    desc=False

    for index in range(len(arr)):

        
        if index == 0:
            if arr[index+1] > arr[index]:
                asc=True
                desc=False
            if arr[index+1] < arr[index]:
                asc=False
                desc=True
        
        if (index != 0) and (index != (len(arr)-1)):
            if (arr[index-1] < arr[index] < arr[index+1]) and asc:
                    asc=True
                    desc=False
            elif (arr[index-1] > arr[index] > arr[index+1]) and desc:
                    asc=False
                    desc=True
            else:
                asc=False
                desc=False
        
        if index == (len(arr)-1):
            if (arr[index-1] < arr[index]) and asc:
                asc=True
                desc=False
            if arr[index-1] < arr[index] and desc:
                asc=False
                desc=True
    
    if asc:
        return 'yes, ascending'
    if desc:
        return 'yes, descending'
    if not asc and  not desc:
        return 'no'


