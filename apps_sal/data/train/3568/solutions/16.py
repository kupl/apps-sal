def bumps(road):
    #I: string
    #O: string
    
    #
    commute = road 
    
    #count bumps
    bumps = commute.count('n')
    
    #summarize filter logic
    condition_1 = bumps < 16
    condition_2 = bumps >= 16 
    
    if condition_1:
        return 'Woohoo!'
    if condition_2:
        return 'Car Dead'
    
    

