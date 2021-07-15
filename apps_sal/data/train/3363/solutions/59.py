def evaporator(content, evap_per_day, threshold,original=None):
    if not original:
        original = content
    if content > original*threshold/100:
        content*=(1-evap_per_day/100)
        return 1 + evaporator(content, evap_per_day, threshold, original)
    return 0
