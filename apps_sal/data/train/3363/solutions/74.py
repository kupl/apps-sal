def evaporator(content, evap_per_day, threshold):
    evap_per_day=(evap_per_day/100)
    threshold=content*(threshold/100)
    total=content
    days=0
    while total > threshold:
        total-=(total*evap_per_day)
        days+=1
    return days
