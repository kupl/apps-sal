def evaporator(content, evap, threshold):
    days = 0
    lost = 100
    while lost >= threshold:
        lost -= lost * evap / 100
        days += 1
    return days
