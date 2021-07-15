def invite_more_women(arr):
    #your code here
    
    count_of_men = 0
    count_of_women = 0
    
    for item in arr:
        if item == 1:
            count_of_men += 1
        else:
            count_of_women += 1
    
    if count_of_men <= count_of_women:
        return False
        
    else:
        return True
    
            
            
    
    

