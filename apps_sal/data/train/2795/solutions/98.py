def cockroach_speed(s):
    import math
    conversion = (1000 * 100)/(60*60)
    speed = math.floor(s*conversion)
    return speed
