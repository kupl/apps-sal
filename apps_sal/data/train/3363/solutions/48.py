def evaporator(content, evap_per_day, threshold):
    x = 0
    y = content
    while y > content * (threshold / 100):
        y = y - y * (evap_per_day / 100)
        x = x + 1
    return x
