def evaporator(content, evap_per_day, threshold):  # Jai Shree Ram!!!
    result = 0
    n = content * threshold / 100
    while content > n:
        content = content - (content * evap_per_day / 100)
        result += 1
    return result
