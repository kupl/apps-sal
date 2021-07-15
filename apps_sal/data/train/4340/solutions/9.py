def shortest_time(speed):
    speed = sorted(speed)
    return min(speed[1]*3+speed[0]+speed[3],speed[0]+sum(speed))
