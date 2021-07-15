def evaporator(content, evap_per_day, threshold):
    new_content = content
    thresh_quant = content * threshold / 100
    n_day_expire = 0
    while new_content > thresh_quant: 
        new_content = new_content - (new_content * (evap_per_day / 100))
        n_day_expire += 1
    return n_day_expire
