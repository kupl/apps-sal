def evaporator(content, evap_per_day, threshold):
    i = 0
    threshold = threshold * 0.01 * content
    while content > threshold:
        i += 1
        content -= content * evap_per_day * 0.01

    return i
