def evaporator(content, evap_per_day, threshold):
    remain = 100.0
    day = 0
    while True:
        day += 1
        remain = remain * (100.0 - evap_per_day) / 100.0
        if remain <= threshold:
            return day
