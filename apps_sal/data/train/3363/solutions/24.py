def evaporator(content, evap_per_day, threshold):
    #It is important to remember that percent is a ratio and content is a volume
    critical_amount=(threshold/100)*content
    n=0
    while content >=critical_amount:
        content=content-(content*(evap_per_day/100))
        n+=1
    return n
        
        
        

