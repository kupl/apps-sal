def fly_by(lamps, drone):
    s1, s2 = len(drone), len(lamps)
    return 'o' * min(s1, s2) + 'x' * (s2 - s1)
