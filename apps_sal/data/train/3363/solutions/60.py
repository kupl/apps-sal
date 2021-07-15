def evaporator(content, evap_per_day, threshold):
    evap_per_day=evap_per_day/100
    threshold=threshold/100
    days=0
    min_content = content*threshold
    while content >= min_content:
        content -= content * evap_per_day
        days += 1
    return days
            
            
        
            

