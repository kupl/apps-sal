def evaporator(content, evap, threshold):
    counter = 0
    threshold = content * (threshold / 100)
    evap = (evap / 100)
    while content >= threshold:
        content -= content * evap
        counter += 1
    return counter
