def evaporator(content, evap_per_day, threshold):
    percentage = 100
    for day in range(10000):
        percentage = percentage * (1 - evap_per_day / 100)
        if percentage < threshold:
            return day + 1
