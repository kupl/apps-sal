def shortest_time(speed):
    speed.sort()
    o = 3 * speed[1] + speed[0] + speed[3]
    t = sum(speed[1:]) + (len(speed) - 2) * speed[0]
    return o if o <= t else t
