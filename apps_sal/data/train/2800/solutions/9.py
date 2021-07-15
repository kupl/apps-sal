from math import cos, pi, sin

SHIP_MPH = 90  # WOW, part trawler - part speed boat, fast ship!
NET_LENGTH = 40  # Impressive net length too, are these fishermen using alien tech?


def find_time_to_break(bearing_A, bearing_B):
    
    # Find angle between ships
    ba, bb = bearing_A + 360, bearing_B + 360
    alpha = min(abs(ba - bb), abs(bb - ba))
    if alpha > 180:
        alpha = 360 - alpha
    
    if alpha == 0:
        # Ships travelling on parallel courses
        return float('inf')
    
    # Find seperation between ships per hour
    theta = alpha / 2 / 180 * pi  # Half alpha in rads
    # Position of each ship
    s1 = SHIP_MPH * sin(theta), SHIP_MPH * cos(theta)
    s2 = SHIP_MPH * sin(-theta), SHIP_MPH * cos(-theta)
    # Pythagorean distance between ships
    mph = (((s1[0] - s2[0]) ** 2) + ((s1[1] - s2[1]) ** 2)) ** 0.5
    
    # Max time in minutes before the net snaps
    return NET_LENGTH / mph * 60

