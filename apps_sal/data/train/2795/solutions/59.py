def cockroach_speed(s):
    import math
    if s == 0:
        return 0
    else:
        meter_per_sec = s / 3.6
        cm_per_sec = meter_per_sec * 100
        return math.floor(cm_per_sec)
