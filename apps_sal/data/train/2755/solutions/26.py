def multiple_of_index(arr):
    result =  []
    n = 0
    while n < len(arr):
        if n != 0 and arr[n] % n ==0:
            result.append(arr[n])
        n+=1
         
    return result
