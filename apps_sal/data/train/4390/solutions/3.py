def fly_by(lamps, drone):
    on = drone.find("T") + 1
    return lamps.replace("x", "o", on)
