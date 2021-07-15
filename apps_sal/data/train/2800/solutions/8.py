from math import sin, pi

def find_time_to_break(bearing_A, bearing_B):
    return float("inf") if abs(bearing_A-bearing_B) == 0 else 20/(sin((abs(bearing_A-bearing_B)*pi/180)/2))*60/90
