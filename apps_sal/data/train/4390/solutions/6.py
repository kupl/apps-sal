def fly_by(lamps, drone):
    os = min(len(drone), len(lamps))
    xs = len(lamps) - len(drone)
    return os * 'o' + xs * 'x'
