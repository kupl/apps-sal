def evaporator(content, evap_per_day, threshold):
    day = []
    not_useful = content * (threshold / 100)
    while content >= not_useful:
        content -= (evap_per_day / 100) * content
        day.append(content)
    return(len(day))
