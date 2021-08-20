def evaporator(content, evap_per_day, threshold):
    days = 0
    contentLeft = content
    while contentLeft > content * (threshold / 100):
        contentLeft = contentLeft * (1 - evap_per_day / 100)
        days += 1
    return days
