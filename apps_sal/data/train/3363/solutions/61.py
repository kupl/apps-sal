def evaporator(content, evap_per_day, threshold):
    
    days = 0
    perc_content = 100
    new_content = content
    
    while perc_content > threshold:
        perct_evp = (evap_per_day / 100) * new_content
        print(perct_evp)
        new_content = new_content - perct_evp 
        print(new_content)
        perc_content = (new_content / content) * 100
        print(perc_content)
        days += 1
    
    return days
