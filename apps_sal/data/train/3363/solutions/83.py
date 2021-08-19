def evaporator(content, evap_per_day, threshold):
    th = threshold / 100
    thres = content * th
    evap = evap_per_day / 100
    count = 0
    while content > thres:
        content = content - content * evap
        count = count + 1
    return count
