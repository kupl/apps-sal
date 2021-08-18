def evaporator(content, evap_per_day, threshold):

    day_counter = 0
    turn_off_level = content * (((threshold / 100)))

    while content > turn_off_level:
        content = content * (1 - (((evap_per_day) / 100)))
        day_counter += 1
    return day_counter


evaporator(10, 10, 10)
