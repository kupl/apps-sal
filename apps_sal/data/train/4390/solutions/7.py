def fly_by(lamps, drone):
    count = len(drone)
    if lamps:
        first_sec = lamps[:count]
        second_sec = lamps[count:]
        final_1st = lamps[:count].replace("x", "o")
        return final_1st + second_sec
