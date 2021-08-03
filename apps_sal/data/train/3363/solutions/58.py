def evaporator(content, evap_per_day, treshold, original=None):
    if not original:
        original = content
    if content > original * treshold / 100:
        content *= (1 - evap_per_day / 100)
        return 1 + evaporator(content, evap_per_day, treshold, original)
    return 0
