def evaporator(content, evap_per_day, threshold):
    days = 1
    new_content = content
    while True:
        new_content = new_content - new_content * evap_per_day * 0.01
        if new_content / content < threshold * 0.01:
            return days
        else:
            days += 1
