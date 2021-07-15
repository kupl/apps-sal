def evaporator(content, evap_per_day, threshold):
    
    counter,threshold =0, content*threshold/100
    while content >= threshold:
        counter+=1
        content-=content*evap_per_day/100
    return counter
