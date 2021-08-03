def evaporator(content, evap_per_day, threshold):
    q_threshold = content * threshold / 100
    days = 0

    while content >= q_threshold:
        q_evap_per_day = content * evap_per_day / 100
        content = content - q_evap_per_day
        days += 1
    return(days)
