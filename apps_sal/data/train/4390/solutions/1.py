def fly_by(lamps, drone):
    l = len(lamps)
    d = len(drone)
    if d >= l:
        return 'o' * l
    return 'o' * d + 'x' * (l - d)
