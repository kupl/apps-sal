def evaporator(content, evap_per_day, threshold):
    percent_of_content = 1
    days = 0
    while percent_of_content > threshold * 0.01:
        days += 1
        percent_of_content -= percent_of_content * evap_per_day * 0.01
    return days
