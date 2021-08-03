def evaporator(content, evap_per_day, threshold):
    mlimit = content * (threshold / 100)
    days = 0
    while content > mlimit:
        content -= content * (evap_per_day / 100)
        days += 1
        print(content)
    return days
