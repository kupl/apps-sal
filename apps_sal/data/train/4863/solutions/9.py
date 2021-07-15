def circularly_sorted(arr):
    smallest = arr.index(min(arr))
    if arr[smallest:] + arr[:smallest] == sorted(arr):
        return True
    else:
        return False
    
            
            
    
    
        
    
        
        

