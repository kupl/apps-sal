def find_smallest_int(arr):
    # Code here
    answer = arr[0]
    
    for nr in arr:
        if nr < answer:
            answer = nr
            
    
    return answer
