def evaporator(content, evap_per_day, threshold):
    content_aux = (content * threshold) / 100
    days = 0
    while content > content_aux:
        content -= (content*evap_per_day)/100
        days += 1
    return days
