def century(year):
    century = 0
    
    # For every 100 years, increment century by 1
    for interval in range(0, year, 100): 
        century += 1  
    return century
