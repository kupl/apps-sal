def london_city_hacker(journey): 
    
    sum = 0.0    
    isBus = False
    
    for i in journey :
        if len(str(i)) <= 3:
            if isBus :
                isBus = 0 
            else :
                sum += 1.50
                isBus = 1
        else :
            sum += 2.40
            isBus = 0
    
    sum = round(sum * 100) / 100
    
    return f'£{str(sum)}0'
