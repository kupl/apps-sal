def evaporator(content, evap_per_day, threshold):

    def p(x):
        return (100 - x) / 100
    x = 100
    times = 0
    while x >= threshold:
        x *= p(evap_per_day)
        times += 1
    return times
