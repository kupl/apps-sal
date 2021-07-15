def evaporator(content, evap_per_day, threshold):
    thres = content * threshold/100
    count = 0
    while content > thres:
        content = content - content * evap_per_day/100
        count += 1
    return count
