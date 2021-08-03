def shortest_time(speed):
    speed.sort()
    return speed[0] + speed[1] + speed[3] + min(2 * speed[1], speed[0] + speed[2])
