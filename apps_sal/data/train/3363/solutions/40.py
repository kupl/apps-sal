def percent_convert(num):
    return num/100

def evaporator(content, evap_per_day, threshold):
    content= 1
    evap_per_day = percent_convert(evap_per_day)
    threshold = percent_convert(threshold)
    day_counter = 0
    while content > threshold:
        content = content * (1 - evap_per_day)
        day_counter+=1
    return day_counter
