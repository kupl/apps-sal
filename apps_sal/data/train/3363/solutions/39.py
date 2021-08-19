def evaporator(content, evap_per_day, threshold):
    result = 0
    percent_change = 100
    while percent_change > threshold:
        percent_change -= percent_change * (evap_per_day / 100)
        result = result + 1
    return result
