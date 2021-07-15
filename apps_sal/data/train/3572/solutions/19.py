def invite_more_women(arr):
    
    women = 0
    men = 0
    
    for i in arr:
        if i == 1:
            men+=1
        if i == -1:
            women+=1
            
    if men > women:
        return True
    else:
        return False
