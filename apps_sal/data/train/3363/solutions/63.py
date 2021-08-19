def evaporator(content, evap_per_day, threshold):
    day = 0
    not_useful = content * (threshold / 100)
    while content >= not_useful:
        content -= evap_per_day / 100 * content
        day += 1
    return day
