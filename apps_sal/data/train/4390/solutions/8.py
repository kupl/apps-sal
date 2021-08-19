def fly_by(lamps, drone):
    return 'o' * min(len(drone), len(lamps)) + lamps[len(drone):]
