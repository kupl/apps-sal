def evaporator(content, evap_per_day, threshold):
    content_pct = 100
    days = 0
    while content_pct > threshold:
        content_pct -= (evap_per_day * content_pct) / 100.0
        days += 1
    return days
