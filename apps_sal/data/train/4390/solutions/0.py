def fly_by(lamps, drone):
    return lamps.replace('x', 'o', drone.count('=') + 1)
