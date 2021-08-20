def evaporator(content, evap_per_day, threshold):
    content = 100
    t = threshold / 100 * content
    epd = evap_per_day / 100
    n = 0
    while content > threshold:
        n += 1
        content *= 1 - epd
    return n
