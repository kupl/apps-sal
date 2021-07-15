def is_centered(arr,n):
    if sum(arr) == n: return True
    for i in range(1,int(len(arr)/2)+1):        
        if sum(arr[i:-i]) == n:
            return True
    return False
