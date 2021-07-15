def is_nice(arr):
    if arr==[]:
       return False
    else:   
        for i in arr:
            if i+1 not in arr:
               if i-1 not in arr:
                    return False
        return True 

