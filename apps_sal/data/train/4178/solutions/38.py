def min_sum(arr):
    total = 0
    lowest_number = int(arr[0])
    biggest_number = int(arr[0])
    while len(arr) > 0:
        for i in arr:
            if i < lowest_number:
                lowest_number = i
            elif i > biggest_number:
                biggest_number = i
            
        total += biggest_number * lowest_number
        
        print(arr)
        
        arr.pop(arr.index(lowest_number))
        arr.pop(arr.index(biggest_number))

        
        if len(arr) >= 2:
            lowest_number = int(arr[0])
            biggest_number = int(arr[0])
        
    return(total)
