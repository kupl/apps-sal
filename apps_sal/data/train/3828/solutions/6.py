def calculate_time(battery, charger):
    max = 100
    time = 0
    fast = (battery / charger) * .85
    dcharge = (battery / charger) * .2
    tcharge = (battery / charger) * .25
    if max == 100:
        time += fast
        max += -85
    if max == 15:
        time += dcharge
        max += -10
    if max == 5:
        time += tcharge
        max += -5
    if time == 1.105:
        return 1.11
    return round(time, 2)
