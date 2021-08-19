def evaporator(content, evap_per_day, threshold):
    a = int(content)
    b = 0
    while content > a / 100 * threshold:
        content = content - content / 100 * evap_per_day
        b += 1
    return b
