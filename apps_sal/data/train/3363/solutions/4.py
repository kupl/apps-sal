def evaporator(content, evap_per_day, threshold):
    thresholdper = threshold / 100
    amount_remaining = content
    days = 0
    while amount_remaining / content >= thresholdper:
        amount_remaining = amount_remaining * (1 - evap_per_day / 100)
        days += 1
    return days
