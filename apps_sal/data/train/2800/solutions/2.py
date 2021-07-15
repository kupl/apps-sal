import math
def find_time_to_break(bearing_A, bearing_B):
    
    ships_angle = abs(bearing_A - bearing_B) * (math.pi/180)
    
    time_to_40 = float('inf')
    if ships_angle > 0:
        den = 1.5 * math.sqrt(2 * (1 - round(math.cos(ships_angle),5)))
        time_to_40 = round(40/den, 2)
    
    return time_to_40
