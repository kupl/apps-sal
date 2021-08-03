def evaporator(content, evap, threshold):
    ilosc = 100
    day = 0
    while ilosc > threshold:
        ilosc = ilosc * (1 - evap / 100)
        day += 1
    return day
