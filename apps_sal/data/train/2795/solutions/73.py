import math

def cockroach_speed(s):
    to_minutes =s/60
    to_secs = to_minutes/60
    return math.floor(to_secs*100000)

