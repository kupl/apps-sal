def sum_array(arr=[0]):
    try:
        if len(arr) > -1 and len(arr) < 3:
            return 0
        else:
            return sum(arr)- (min(arr)+max(arr))
    
    except:
        return 0 
